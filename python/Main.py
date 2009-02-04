###############################################################################
# Main.py
# 
# PHY1234, Automne 2005
# Rapport de laboratoire 12
# 3 decembre 2005
# Philippe Chretien (CHRP11037001)
# http://www.philippe-chretien.com/PHY1234/lab12.zip
###############################################################################

from time import *
from Fourmi import *
from Domaine import *
from Position import *
from Tkinter import *

# Pas de temps pour la simulation en secondes
dt = 1.

# Distance entre deux cellules du domaine en cm
dx = 1.

# Nombre de fourmis dans la colonie
nombre_de_fourmis = 40

# Position du nid de fourmis dans le domaine
position_du_nid = Position( 5,5 )

# Dimensions du domaine
lx = 25
ly = 20

# Position de la nouriture ...
hg = Position(20,8)
bd = Position(24,12)

# Position de la nouriture ... apres 1000sec
hg2 = Position(3,17)
bd2 = Position(7,19)

# Objet de gestion du parametre de source
source = SourceEvaporation( 0.01 )

# Domaine dans lequel evoluent les fourmis
domaine = Domaine( lx, ly, dx, dt, source, hg, bd, 0.02, 1., hg2, bd2 )

fourmiList = []
for i in range(nombre_de_fourmis):
	fourmiList.append( Fourmi( domaine, position_du_nid, 2, 8 ) )
	
###############################################################################
# Graphique
###############################################################################
def gogogo():
	for i in range( 2000 ):
		# Pour doner une chance au CPU
		sleep(0.001)
		
		# On reset la form
		canevas.delete("all")
		
		# Calcul de la diffusion et de l'evaporation
		domaine.euler()
		
		# Calcul du deplacement des fourmis
		for i in range(nombre_de_fourmis):
			fourmiList[i].bouge()
		
		# Calcul de l'interraction des fourmis sur le domaine
		for i in range(nombre_de_fourmis):
			fourmiList[i].modifieEnvironnement()		
			
		# Affichage des zones saturees en pheromones
		for y in range( domaine.ny ):
			for x in range( domaine.nx ):
				if( domaine.n[x][y] > domaine.maxPheromones - ( 0.25 * domaine.maxPheromones ) ):
					canevas.create_rectangle((x*40)+40,(y*10)+44,(x*40)+80,(y*10)+34,fill='green')

		# Dessine la nouriture initiale
		x = (hg.x*40)+40
		y = (hg.y*10)+36
		dx = (bd.x-hg.x+1)*40
		dy = (hg.y-bd.y-1)*10
		canevas.create_rectangle(x,y,x+dx,y-dy,fill='red')
		
		# Dessine la nouriture apres 1000 sec
		if( domaine.t > 1000 ):
			x = (hg2.x*40)+40
			y = (hg2.y*10)+36
			dx = (bd2.x-hg2.x+1)*40
			dy = (hg2.y-bd2.y-1)*10
			canevas.create_rectangle(x,y,x+dx,y-dy,fill='red')

		# Dessine les fourmis
		for i in range(nombre_de_fourmis):
			x = (fourmiList[i].position.x*40)+40
			y = (fourmiList[i].position.y*10)+36
			if( fourmiList[i].mode == 1 ):
				canevas.create_oval(x,y,x+20,y+8,fill='yellow',outline='')
			else:
				canevas.create_oval(x+20,y,x+40,y+8,fill='blue',outline='')
			
		

		# Dessine le nid
		x = (position_du_nid.x*40)+40
		y = (position_du_nid.y*10)+36
		canevas.create_oval(x,y,x+40,y+8,fill='brown')
		
		# Cree la grille avec les taux de pheromone
		for y in range( domaine.ny ):
			for x in range( domaine.nx ):
				cell_value = "%2.4f"%(domaine.n[x][y])
				canevas.create_text((40*x)+40, (10*y)+40,
						 font=("Geneva",8), 
						 text=cell_value, 
						 anchor="w")
		
		# Ecrit les resultats a l'ecran
		resultats_texte = "Recolte=%d   Temps=%ds   Temps a trouver nourriture = %d"%(Fourmi.total_nouriture,domaine.t,domaine.temps_trouver_nourriture)
		canevas.create_text(40,260,
				font=("Geneva",20), 
				text=resultats_texte, 
				anchor="w")

		canevas.update()


# Poutine Tkinter volee au programme Boite.py
fenetre = Tk()
gui = Frame(fenetre)
gui.pack(side=BOTTOM)
canevas = Canvas(fenetre,width=1080,height=300,background='white')

gui.quitter  = Button(gui,text='Quitter',command=gui.quit)
gui.go = Button(gui,text='Go',command=gogogo )

gui.quitter.pack(side=LEFT)
gui.go.pack(side=LEFT)

canevas.pack(expand=YES,fill=BOTH)
fenetre.mainloop()

