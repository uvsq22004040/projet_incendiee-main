##################################
# groupe 3 MIASHS TD2
# Sana MAREF
# Judith FAUCON
# Jalis LACHEHAB
# Rosary NITHIYANANTHAM
# Anya BOUBCHIR
# Nolwenn GAUTIER
# https://github.com/uvsq22004040/projet_incendie.git
######################################################### 

############################
# IMPORTATION DES LIBRAIRIES

import tkinter as tk
import copy
import random

########################
# CONSTANTES
 
COULEUR_FOND = "white"
COULEUR_QUADR = "black"
LARGEUR = 500
HAUTEUR = 500
COTE = 15
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE
TAILLE_CARRE = LARGEUR // NB_LINE
 
 
######################
# Variables globales
 
tableau = None
 
########################
# FONCTIONS
 
 
def quadrillage():
    """Affiche un quadrillage sur le canvas."""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE
 
 
    """Affiche un quadrillage sur le canvas."""
    colors = ["yellow2", "chartreuse3", "steelblue1"]
    for i in range(NB_LINE):
        for j in range(NB_COL):
            canvas.create_rectangle((i*TAILLE_CARRE, j*TAILLE_CARRE),((i+1)*TAILLE_CARRE, (j+1)*TAILLE_CARRE),
             outline="black", fill=random.choices(colors))
 
 
def coord_to_lg(x, y):
    """Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y"""
    return x // COTE, y // COTE
 
 
def change_carre(event):
    """Change l'état du carré sur lequel on a cliqué"""
    i, j = coord_to_lg(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle(x, y, x + COTE,
                                        y + COTE, fill='red',
                                        outline=COULEUR_QUADR)
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = -1
 
 
def creer_tableau():
    """initialise un tableau à deux dimensions qui vaut -1 partout
    -1 est pour une case morte
    identifiant du carré dessiné si une case est vivante
    tableau[i][j] est la valeur de la case à la colonne i et la ligne j
    """
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1] * NB_LINE)
    # tableau = [tableau_col for i in range(NB_COL)]
 
 
def traite_case(i, j):
    """Traite la case à la colonne i et ligne j en retournant la nouvelle valeur du tableau"""
    nb_vivant = compte_vivant(i, j)
    if tableau[i][j] == -1:
        if nb_vivant == 3:
            x, y = i * COTE, j * COTE
            carre = canvas.create_rectangle(x, y, x + COTE,
                                            y + COTE, fill=COULEUR_VIVANT,
                                            outline=COULEUR_QUADR)
            return carre
        else:
            return -1
    else:
        if nb_vivant != 2 and nb_vivant != 3:
            canvas.delete(tableau[i][j])
            return -1
        else:
            return tableau[i][j]

 
def annule_tout():
    canvas.delete(quadrillage())

 
########################
# PROGRAMME PRINCIPAL
 
racine = tk.Tk()
racine.title("Incendie")
# création des widgets
first_button = tk.Button(racine, text="Créer un nouveau monde", command=quadrillage)
second_button = tk.Button(racine, text="Recommencer", command=annule_tout)
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)

# placement des widgets
canvas.grid(row=0, column=0)
first_button.grid(row= 1,column=0)
second_button.grid(row=2, column=0)
# liaison des événements
creer_tableau()
canvas.bind("<Button-1>", change_carre)
# boucle principale
racine.mainloop()