###############################################################################
# test.py
# 
# PHY1234, Automne 2005
# Rapport de laboratoire 12
# 3 decembre 2005
# Philippe Chretien (CHRP11037001)
# http://www.philippe-chretien.com/PHY1234/lab12.zip
###############################################################################

from Fourmi import *
from Domaine import *
from Position import *

dt = 1.
dx = 1.

# Dimensions du domaine
lx = 10
ly = 10

# Position de la nouriture ...
hg = Position(2,2)
bd = Position(2,3)

# Nid
position_du_nid = Position( 5,5 )

# Objet de gestion du parametre de source
source = SourceSansEffet(0)

# Domaine dans lequel evoluent la fourmi
domaine = Domaine( lx, ly, dx, dt, source, hg, bd, 0.02, 10. )
domaine.n[4][4] = 1
domaine.n[5][4] = 2
domaine.n[6][4] = 3

domaine.n[4][5] = 4
domaine.n[5][5] = 0
domaine.n[6][5] = 5

domaine.n[4][6] = 6
domaine.n[5][6] = 7
domaine.n[6][6] = 8

# Une fourmi
fourmi = Fourmi( domaine, position_du_nid, 1, 1 )
fourmi.bouge()

fourmi = Fourmi( domaine, position_du_nid, 1, 1 )
fourmi.mode = 1
fourmi.positionNid = Position(5,3)
fourmi.bouge()

p1 = Position(5,4)
p2 = Position(5,3)
print p1.distance(p2)
