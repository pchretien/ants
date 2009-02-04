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
