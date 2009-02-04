###############################################################################
# Position.py
# 
# PHY1234, Automne 2005
# Rapport de laboratoire 12
# 3 decembre 2005
# Philippe Chretien (CHRP11037001)
# http://www.philippe-chretien.com/PHY1234/lab12.zip
###############################################################################

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
		