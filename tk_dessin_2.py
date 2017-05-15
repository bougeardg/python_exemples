# -$- coding:Utf-8 -*
from tkinter import *


def couleur(r,g,b):
    #conversion en hexadécimal puis on enlève les deux premiers caractères "0x"
    r=hex(r)[2:]
    g=hex(g)[2:]
    b=hex(b)[2:]
    k=len(r)
    if k==1:
        k=k+1
    if len(g)>k:
        k=len(g)
    if len(b)>k:
       k=len(b)
    for i in range(0,k-len(r)):
       r="0"+r
    for i in range(0,k-len(g)):
       g="0"+g
    for i in range(0,k-len(b)):
       b="0"+b
    return "#"+r+g+b
# Création de la fenêtre principale (main window)
fenetre = Tk()
#titre de la barre au dessus de la fenêtre
fenetre.title('Premier dessin')
#création d'un canvas qui sera une zone pour le dessin
#bg pour la couleur de fond et bd pour la taille de la bordure
#qui sera de la couleur du fond
zone_dessin=Canvas(fenetre,scrollregion=(0,0,500,500),width=500,height=500,border=0)
#affichage de la zone
for i in range(0,500):
    strcol=couleur(int((i/500.)*255.),int((i/500.)*255.),int((i/500.)*255.))
    zone_dessin.create_line(i,0,i,499,fill=strcol,width=1)
   # print(int((i/500.)*255.))

zone_dessin.grid()

# lancement de la boucle tkinter
fenetre.mainloop()
