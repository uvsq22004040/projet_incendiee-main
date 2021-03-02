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


############################
# CONSTANTES

LARGEUR = 480
HAUTEUR = 480
COTE_CARRE = LARGEUR // 30
COULEUR_FOND = "white"

############################
# FONCTIONS

def quadrillage():
    """Affiche un quadrillage"""
    for i in range(30):
        for j in range(30):
            canvas.create_rectangle((i*COTE_CARRE, j*COTE_CARRE),((i+1)*COTE_CARRE, (j+1)*COTE_CARRE), outline="black")


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