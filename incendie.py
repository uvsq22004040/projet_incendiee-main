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
import random


############################
# CONSTANTES

LARGEUR = 480
HAUTEUR = 480
COULEUR_FOND = "white"
NB_LIGNES = 30
NB_COL = 30
COTE_CARRE = LARGEUR // NB_COL

############################
# FONCTIONS

def quadrillage():
    """Affiche un quadrillage de parcelles colorées"""
    colors = ["yellow","green","blue"]
    for i in range(NB_LIGNES):
        for j in range(NB_COL):
            canvas.create_rectangle((i*COTE_CARRE, j*COTE_CARRE),((i+1)*COTE_CARRE, (j+1)*COTE_CARRE), outline="black", fill=random.choices(colors))




############################
# PROGRAMME PRINCIPAL

racine = tk.Tk()
racine.title("Incendie")
# Création des widgets
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg=COULEUR_FOND)
quadrillage()
# Placement des widgets
canvas.grid()
# Boucle principale
racine.mainloop()