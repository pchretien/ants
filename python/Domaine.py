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

from Source import *
from MesMethodes import *

	
class Domaine:
	lx = 0	# longueur du domaine en cm
	ly = 0	# largeur du domaine en cm
	dx = 0.	# pas de la discretisation spatialle en cm
	dt = 0.	# pas de la discretisation temporelle en secondes
	nx = 0	# nombre de points de discretisation dans la direction x
	ny = 0	# nombre de points de discretisation dans la direction y
	K  = 1.	# constante de diffusion en cm^2/s
	t  = 0	# temps ecoule depuis le debut de la simulation en secondes
	n  = 0	# array bidimensionnel de taille nx * ny contenant la valeur
		# de n a chaque point de discretisation
			
	source_object = None	# Objet source qui implemente le comportement de la source
	nouriture_hg = None
	nouriture_bd = None	
	nouriture_hg2 = None
	nouriture_bd2 = None	
	maxPheromones = 1.
	
	# Initialise l'objet Domaine.
	#
	# lx		Largeur du domaine en cm
	# ly		Longueur du domaine en cm
	# dx		Dimension d<une cellule du domaine
	# dt		Pas de temps de l'integration
	# source	Objet implementant le comportement de la source
	# nouriture_hg	Objet Position pointant sur le coin haut gauche de la 
	#		nouriture dans le domaine
	# nouriture_bd	Objet Position pointant sur le coin bas droit de la 
	#		nouriture dans le domaine
	def __init__( self, lx, ly, dx, dt, source, nouriture_hg, nouriture_bd, K, maxPheromones, nouriture_hg2, nouriture_bd2 ):
		self.lx = lx
		self.ly = ly
		self.dx = float(dx)
		self.dt = float(dt)
		self.nx = int(lx / dx)
		self.ny = int(ly / dx)
		self.K = K
		self.n = None
		self.t = 0
		self.n = zeros( (self.nx, self.ny), float)
				
		self.source_object = source
		self.nouriture_hg = nouriture_hg
		self.nouriture_bd = nouriture_bd
		self.nouriture_hg2 = nouriture_hg2
		self.nouriture_bd2 = nouriture_bd2
		self.maxPheromones = maxPheromones
		
		self.temps_trouver_nourriture = 0
	
	# Calcul le laplacien pour le calcul de la diffusion 
	def laplace( self ):
		# Cree une matrice vide
		laplace = zeros( (self.nx, self.ny), float )
		
		# Calcul du laplacien pour chaque cellule
		for j in range( self.ny ):
			for i in range( self.nx ):
				# Condition aux limites ... rien a calculer
				if( i == 0 or j == 0 or i == self.nx-1 or j == self.ny-1 ):
					continue
				
				laplace[i][j] += self.n[i+1][j]
				laplace[i][j] += self.n[i-1][j]
				laplace[i][j] += self.n[i][j+1]
				laplace[i][j] += self.n[i][j-1]
				laplace[i][j] -= 4*self.n[i][j]
				laplace[i][j] *= self.K
				laplace[i][j] /= self.dx
				
		# On retourne la matrice
		return laplace
		
	# Calcul le terme de source de l'equation.
	# C'est la responsabilite de l'objet source
	def source( self ):
		return self.source_object.source( self.n, self.nx, self.ny, self.dt )
	
	# Boucle principale d'integration
	def euler( self ):
		# Pour chaque pas de temps demande le laplacien ...
		laplace = self.laplace()
		# ... la source
		source = self.source()		

		# ... et multiplie les deux par le dt pour ajouter le tout a
		# la matrice principale "n"
		self.n += laplace*self.dt + source*self.dt

		# Incremente le temps total
		self.t += self.dt		
		
		return True

	# Permet aux fourmis d'ajouter des pheromones au domaine			
	def ajoutePheromones( self, position, ph ):
		self.n[position.x][position.y] += ph
		if( self.n[position.x][position.y] > self.maxPheromones ):
			self.n[position.x][position.y] = self.maxPheromones
		
	# NOTE: Pour ne pas retourner d'erreur il faut eviter d'appeler cette
	# fonction avec une position aux limites du domaine.
	def environnementLocal( self, position ):
		ret = self.n[position.x-1:position.x+2,position.y-1:position.y+2]
		return ret
		
	# Retourne True si les coordonnees recues se trouvent dans une zone ou il y a
	# de la nourriture
	def contientNouriture( self, position ):
		# Verifie pour la nouriture initiale
		if( position.x >= self.nouriture_hg.x and position.x <= self.nouriture_bd.x and position.y >= self.nouriture_hg.y and position.y <= self.nouriture_bd.y ):
			return True
			
		# Verifie pour la nourriture apres 1000 sec
		if( self.t > 1000 ):
			if( position.x >= self.nouriture_hg2.x and position.x <= self.nouriture_bd2.x and position.y >= self.nouriture_hg2.y and position.y <= self.nouriture_bd2.y ):
				if( self.temps_trouver_nourriture == 0 ):
					self.temps_trouver_nourriture = self.t - 1000
				return True
			
		return False
		
	