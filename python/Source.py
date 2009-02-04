###############################################################################
# Source.py
# 
# PHY1234, Automne 2005
# Rapport de laboratoire 12
# 3 decembre 2005
# Philippe Chretien (CHRP11037001)
# http://www.philippe-chretien.com/PHY1234/lab12.zip
###############################################################################

import sys
from math import *
from random import *
from numpy import *

# Un calcul de la source qui ne produit aucun effet pour les tests
# unitaires avant utilisation du programme.
class SourceSansEffet:
	evaporation = 0.

	def __init__( self, evaporation=0. ):
		self.evaporation = evaporation

	def source( self, n, nx, ny, dt ):
		source = zeros( (nx, ny), float )
		return source

# Cette classe "sour contracte" le calcul du terme de source
# dans le calcul de la diffusion et evaporation
class SourceEvaporation:
	evaporation = 0.

	# Constructor
	def __init__( self, evaporation=0. ):
		self.evaporation = evaporation

	# Calcul le terme de source pour le domaine n
	# Seule l<evaporation est prise en compte.
	def source( self, n, nx, ny, dt ):
		source = zeros( (nx, ny), float )
		for j in range(ny):
			for i in range(nx):
				source[i][j] += n[i][j] * self.evaporation * -1.

		return source
