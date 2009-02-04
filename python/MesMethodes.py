###############################################################################
# MesMethodes.py
# 
# PHY1234, Automne 2005
# Rapport de laboratoire 12
# 3 decembre 2005
# Philippe Chretien (CHRP11037001)
# http://www.philippe-chretien.com/PHY1234/lab12.zip
###############################################################################

import math

###############################################################################
# Cette fonction lit un fichier contenant N colonnes de nombres entiers ou 
# reels et retourne une liste de colonnes (listes de valeurs)
#
# filename: 	Le nom du fichier a lire
# return:	La fonction retourne une liste de listes de valeurs reels. 
#		Chaque liste de nombres reels represente une colonne du 
#		fichier d'entree.
###############################################################################
def lectureListesReels( filename ):
	# Initialisons la liste qui sera retournee
	ret = []
	
	# Ouvrons le fichier en lecture
	file = open( filename, "r" )
	
	# Nous lisons toutes les lignes du fichier d'un coup
	lines = file.readlines()
	
	# Fermons immediatement le fichier pour retourner les ressources au 
	# systeme. Le moins longtemps on le garde le ouvert le mieux c'est.
	file.close()
	
	# Ce flag nous permet de savoir si nous sommes a la premiere ligne du 
	# fichier
	first_line = True
	
	# Maintenant il faut boucler sur toutes les lignes pour en extraire les
	# valeurs.	
	for line in lines:
		text_columns = line.split()
		
		for i in range( len(text_columns) ):
			# La premiere ligne nous permet de creer toutes les 
			# colonnes necessaires en prenant pour acquis que 
			# toutes les lignes contiennent le meme nombre de 
			# colonnes
			if first_line :
				column = [float(text_columns[i])]
				ret.append( column )
			else:
			# Pour les autres lignes nous ne faisons que concatener
			# les nouvelles valeurs aux colonnes deja crees
				ret[i].append(float(text_columns[i]))
				
		# Remettons la valeur a False pour toutes les autres lignes du
		# fichier
		first_line = False

	# Retournons la liste de colonnes (listes de valeurs)
	return ret

###############################################################################
# Cette fonction ecrit dans un fichier le contenu d'un nombre N de colonnes
# contenant un nombre M de lignes. Les valeurs sont ecrites dans le fichier 
# sont des entiers ou des reels et sont ecrits en format scientifique.
#
# filename:	Nom du fichier dans lequel sauver le\es donnees
# columns: 	Donnees a sauver dans le fichier. Les donnees doivent etre 
#		recues comme une liste de liste de nombres entiers ou reels.
# return: 	La fonction ne retourne rien
###############################################################################
def ecritureListesReels( filename, columns ):
	# Preparons les lignes a ecrire avant d'ouvrir le fichier de sortie
	text_lines = []
	
	# Nombre de lignes et de colonnes a traiter
	number_of_columns = len( columns )
	number_of_lines = len( columns[0] )
	
	# Boucle dans toutes les lignes 
	for line in range( number_of_lines ):
		# Initialisons la ligne de texte
		text_line = ""	
		
		# Ajoutons les colonnes a la ligne
		for column in range( number_of_columns ):
#			text_line += "%E"%columns[column][line] + " "
			text_line += "%0.4f"%columns[column][line] + " "
		
		# Enlevons l'espace de trop de la derniere colonne
		text_line = text_line.strip()
		
		# Ajoutons un retour de chariot (ligne)
		text_line += "\n"
		
		# Finalement ajoutons la ligne a la liste de lignes
		text_lines.append( text_line )
		
	# Il est temps d'ouvrir le fichier de sortie
	file = open( filename, "w" )
	
	# Ecrivons toutes les lignes d'un seul coup
	file.writelines( text_lines )
	
	# Ne jamais oublier de fermer le fichier pour retourner les ressources
	# au systeme d'exploitation
	file.close()
	
	# La fonction ne retourne rien


###############################################################################
# Cette fonction calcule lla moyenne d'une liste de nombres reels et d'entiers
#
# numbers:	Liste de nombres reels ou entiers dont on veut faire la moyenne
# return: 	La moyenne des valeurs de la liste passee en parametre
###############################################################################	
def moyenneListeReels( numbers ):
	# Initialisons le resultat a retourner
	average = 0.0
	
	# Une boucle pour additionner toutes les valeurs de la liste numbers
	for number in numbers:
		average += number
		
	# La moyenne etant le\a somme sur le nombre d'elements ... on divise la
	# somme par la longueur de la liste
	average /= len( numbers )
	
	# On retourne le resultat a l'appelant
	return average

###############################################################################
# Cette fonction calcule l'ecart type d'une liste de nombres reels et d'entiers
#
# numbers:	Liste de nombres reels et entiers dont on veut calculer l'ecart 
#		type
# return: 	L'ecart type des valeurs de la liste passee en parametre
###############################################################################		
def ecartTypeListeReels( numbers ):
	# Initialisons la valeur de retour
	ecart = 0.0
	
	# Nous avons besoin du nombre d'items dans la liste et de la moyenne
	# des nombres de la liste
	N = len( numbers )
	x = moyenneListeReels( numbers )
	
	# Initialisons la somme des termes (xi-x)**2
	somme = 0.0
	
	# Boucle sur tous les nombres de la liste pour calculer la somme des
	# termes (xi-x)**2
	for number in numbers:
		somme += (number-x)**2
	
	# Finalisation du calcul de l'ecart type ...
	ecart = math.sqrt( somme / float(N) )
	
	# Nous retournons l'ecart type calcule a l'appelant
	return ecart
	

###############################################################################
# Cette fonction calcule a la fois la moyenne et l'ecart type d'une liste de
# nombres reels et d'entiers.
#
# numbers:	Liste de nombres reels ou entiers dont on veut calculer l'ecart 
#		type et la moyenne
# return: 	L'ecart type et la moyenne des valeurs de la liste passee en 
#		parametre
###############################################################################		
def moyenneEcartTypeListeReels( numbers ):
	# Initialisons le resultat de la moyenne a retourner
	average = 0.0
	
	# initialisation de la moyenne des nombres au carre de la liste
	average2 = 0.0
		
	# Une boucle pour additionner toutes les valeurs de la liste numbers
	for number in numbers:
		average += number
		average2 += number**2
			
	# La moyenne etant la somme sur le nombre d'elements ... on divise la
	# somme par la longueur de la liste
	average /= len( numbers )
	average2 /= len( numbers )
	
	# Finalisation du calcul de l'ecart type ...
	ecart = math.sqrt( average2 - average**2 )
	
	# Nous retournons l'ecart type calcule a l'appelant
	return average, ecart

###############################################################################
# Cette fonction recursive calcule la somme d'une liste de nombres reels et 
# d'entiers
#
# numbers:	Liste de nombres reels ou entiers dont on veut faire la moyenne
# return: 	La moyenne des valeurs de la liste passee en parametre
###############################################################################		
def sommeRecursiveListeReels( numbers ):
	# Si nous sommes au dernier element de la liste ...
	if len(numbers) == 1:
		return numbers[0]
	# Sinon nous retournons la somme du premier element et additionne a la
	# somme du reste de la liste en rappelant la methode 
	# sommeRecursiveListeReels avec la sous liste [1:]
	return numbers[0] + sommeRecursiveListeReels( numbers[1:] )
	
###############################################################################
# Cette fonction calcule la moyenne d'une liste de nombres reels et d'entiers
# en faisant appel a la fonction recursive sommeRecursiveListeReels
#
# numbers:	Liste de nombres reels ou entiers dont on veut faire la moyenne
# return: 	La moyenne des valeurs de la liste passee en parametre
###############################################################################		
def moyenneRecursiveListeReels( numbers ):
	# Calcul de la somme de facon recursive
	somme = sommeRecursiveListeReels( numbers )
	# Retour de la somme divisee par le nombre d'elements
	return (somme / float(len(numbers)) )
	

###############################################################################
###############################################################################
# Les methodes qui suivent offrent les memes services que les precedentes en
# utilisant des arrays plutot que des listes. Pour eviter des copies inutiles
# des methodes existantes les methodes utilisant des arrays ne sont que des 
# encapsulations d'appels aux methodes utilisant des listes. Cette pratique
# evite le "cut & paste" abusif et rend la maintenance du code beaucoup plus 
# simple en gardant la logique a un seul endroit.
###############################################################################
###############################################################################
from numpy import *

###############################################################################
# Cette fonction lit un fichier contenant N colonnes de nombres entiers ou 
# reels et retourne un array
#
# filename: 	Le nom du fichier a lire
# return:	La fonction retourne un array de valeurs reels. 
###############################################################################
def lectureArraysReels( filename ):
	ret = lectureListesReels( filename )
	return array( ret )
	
###############################################################################
# Cette fonction ecrit dans un fichier le contenu d'un array. Les valeurs sont 
# ecrites dans le fichier sont des entiers ou des reels et sont ecrits en 
# format scientifique.
#
# filename:	Nom du fichier dans lequel sauver les donnees
# columns: 	Donnees a sauver dans le fichier. Les donnees doivent etre 
#		recues comme un array de nombres entiers ou reels.
# return: 	La fonction ne retourne rien
###############################################################################
def ecritureArraysReels( filename, columns ):
	ecritureListesReels( filename, columns.tolist() )
	
###############################################################################
# Cette fonction calcule lla moyenne d'une liste de nombres reels et d'entiers
#
# numbers:	Array de nombres reels ou entiers dont on veut faire la moyenne
# return: 	La moyenne des valeurs de l'array recu en parametre
###############################################################################	
def moyenneArrayReels( numbers ):
	return moyenneListeReels( numbers )
	
###############################################################################
# Cette fonction calcule l'ecart type d'un array de nombres reels et d'entiers
#
# numbers:	Array de nombres reels et entiers dont on veut calculer l'ecart 
#		type
# return: 	L'ecart type des valeurs de l'array recu en parametre
###############################################################################		
def ecartTypeArrayReels( numbers ):
	return ecartTypeListeReels( numbers )
	

###############################################################################
# Cette fonction calcule a la fois la moyenne et l'ecart type d'un array de
# nombres reels et d'entiers.
#
# numbers:	Array de nombres reels ou entiers dont on veut calculer l'ecart 
#		type et la moyenne
# return: 	L'ecart type et la moyenne des valeurs de l'array recu en 
#		parametre
###############################################################################		
def moyenneEcartTypeArrayReels( numbers ):
	return moyenneEcartTypeListeReels( numbers )

###############################################################################
# Cette fonction recursive calcule la somme d'un array de nombres reels et 
# d'entiers
#
# numbers:	Array de nombres reels ou entiers dont on veut faire la moyenne
# return: 	La moyenne des valeurs de l'array recu en parametre
###############################################################################		
def sommeRecursiveArrayReels( numbers ):
	return sommeRecursiveListeReels( numbers )
	
###############################################################################
# Cette fonction calcule la moyenne d'un array de nombres reels et d'entiers
# en faisant appel a la fonction recursive sommeRecursiveArrayReels
#
# numbers:	Array de nombres reels ou entiers dont on veut faire la moyenne
# return: 	La moyenne des valeurs de l'array recu en parametre
###############################################################################		
def moyenneRecursiveArrayReels( numbers ):
	return moyenneRecursiveListeReels( numbers )
	
