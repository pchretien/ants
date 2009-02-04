## ants ##
#
# This program simulates an ants colony.
# Copyright (C) 2008,2009  Philippe Chretien
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License Version 2
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# You will find the latest version of this code at the following address:
# http://github.com/pchretien
#
# You can contact me at the following email address:
# philippe.chretien@gmail.com


import sys
from math import *
from random import *
from numpy import *

from Position import *
from Domaine import *
from MesMethodes import *

# Classe Fourmi
# Cette classe modelise le comportement d'une fourmi en interraction avec
# son environnement.
class Fourmi:
	domaine = None		# Un objet de type Domaine qui gere les taux de
				# pheromones dans l'environnement de la fourmi 
				# et les positions des sources de nouriture.
	position = None		# Position de la fourmi
	positionNid = None	# Position du nid de fourmis
	mode = 0		# mode = 0 Cherche de la nouriture
				# mode = 1 Rapporte la nouriture au nid
	
	# Parametres pour le calcul des probalite de deplacement des fourmis
	s0 = 1.0		
	s1 = 0.01			
	b0 = 1
	b1 = 8
	
	# Quantite de pheromones emises a chaque seconde
	emission_pheromones = 1.
	
	# Constante des mouvements en fonction de la case choisie ...
	# 0 1 2
	# 3 O 4
	# 5 6 7
	mouvement_x = [-1,0,1,-1,1,-1,0,1]
	mouvement_y = [-1,-1,-1,0,0,1,1,1]
	
	# Offsets accocies aux 8 cellules entourrant la fourmi
	delta_distances_x = array([ [-1,0,1],[-1,0,1],[-1,0,1] ])
	delta_distances_y = array([ [-1,-1,-1],[0,0,0],[1,1,1] ])
	
	# Quantite totale de nourriture amassee par toutes les fourmis
	total_nouriture = 0
	
	# Constructeur de la classe Fourmi
	# Initialisation de toutes les variables internes de l'objet au
	# moment de sa creation.
	#
	# domaine	Un objet de type Domaine qui gere les taux de 
	#		pheromones dans l'environnement de la fourmi et les 
	#		positions des sources de nouriture.
	# positionNid	Position en X et en Y du nid de fourmis
	def __init__( self, domaine, positionNid, b0, b1 ):
		self.domaine = domaine
		self.position = Position( positionNid.x, positionNid.y )
		self.positionNid = Position( positionNid.x, positionNid.y )
		self.mode = 0
		
		# Parametres de calcul des probabilites de mouvement
		self.s0 = 1.0
		self.s1 = 0.01		
		self.b0 = b0
		self.b1 = b1
	
	# Commande a la fourmi de se deplacer en fonction du taux de pheromones
	# ou en fonction de l'emplacement de son nid.
	def bouge( self ):
		# Demande les taux de pheromone au domaine
		local = self.domaine.environnementLocal( self.position )
						
		# Cree la matrice des probabilites de mouvement ...
		P = zeros( (3,3), float )
		
		# On boucle pour remplir la matrice des probabilites
		for j in range(3):
			for i in range(3):
				# On saute la case centrale 
				if( i == 1 and j == 1 ):
					continue
					
				# Action differente en fonction du mode
				if( self.mode == 0 ):
					# Probabilites de mouvement en fonction
					# des pheromones
					P[j][i] = (local[i][j] + self.s0 )**self.b0
				else:
					# On calcul les probabilites pour 
					# retourner au nid
					x = self.position.x + self.delta_distances_x[j][i]
					y = self.position.y + self.delta_distances_y[j][i]
					
					position_cellule = Position(x,y)
					distance_du_nid = position_cellule.distance( self.positionNid )
					
					P[j][i] = 1./(distance_du_nid + 1. + self.s1 )**self.b1
					
		# Maintenant on normalise les probalites ...
		somme = sum(sum( P ))
		for j in range(3):
			for i in range(3):
				if( somme == 0 ):
					P[i][j] = 1./8.
				else:
					P[i][j] /= somme

		# On convertit les probabilites en une liste de 8 elements
		P = reshape( P, (1,9) ).tolist()[0]
		del P[4]
		
#		DEBUG
#		if( self.mode == 1 ):
#			string_P = ""			
#			for i in range(len(P)):
#				string_P += "%0.6f "%P[i]
#			print string_P
		
		# Fait la somme cumulative des probabilites ... 
		# La derniere cellule doit contenir 1.
		for i in range(1,len(P)):
			P[i] += P[i-1]

		# Nous avons notre vecteur de probabilites ...
		r = Random().random()
		
		# Choix au hasard pour prendre la decision de la direction
		index = 0
		for i in range(len(P)):
			if( r < P[i] ):
				index = i
				break;

#		DEBUG
#		if( self.mode == 0 ):
#			print index
#			print self.mouvement_x[index]
#			print self.mouvement_y[index]
		
		# On deplace la fourmie
		self.position.x += self.mouvement_x[index]
		self.position.y += self.mouvement_y[index]
		
		# Verifie les conditions aux limites
		if( self.position.x < 1 ):
			self.position.x = 1
		if( self.position.x > self.domaine.nx-2 ):
			self.position.x = self.domaine.nx-2
			
		if( self.position.y < 1 ):
			self.position.y = 1
		if( self.position.y > self.domaine.ny-2 ):
			self.position.y = self.domaine.ny-2
		
	# Demande a la fourmi d'emetre des pheromones dans le domaine a la
	# position qu'elle occupe.
	def modifieEnvironnement( self ):
		# Si on cherche de la nourriture et qu'on en trouve ...
		if( self.mode == 0 and self.domaine.contientNouriture( self.position ) ):
			self.mode = 1
		# ...ou si on en a deja et qu'on emet des pheromones ...
		elif( self.mode == 1 ):
			self.domaine.ajoutePheromones( self.position, self.emission_pheromones )
			# ou qu'on arrive au nid ...
			if( self.position.equals( self.positionNid ) ):
				self.mode = 0
				Fourmi.total_nouriture += 1
				
			
		