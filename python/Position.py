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


from math import *

# Cette classe definit une position et offre des outils
# de calcul des distances a l'origine ou par rapport a
# un autre objet position
class Position:
	x=0
	y=0
	
	def __init__( self, x, y ):
		self.x = x
		self.y = y
	
	# Distance a l'origine
	def longueur( self ):
		return sqrt(self.x**2+self.y**2)
	
	# Distance d'un autre Position
	def distance( self, position ):
		return sqrt((position.x-self.x)**2 + (position.y-self.y)**2)
	
	# Compare le contenu de deux objets Position
	def equals( self, position ):
		if( self.x == position.x and self.y == position.y ):
			return True
		return False
		