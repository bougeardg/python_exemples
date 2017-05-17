# -$- coding:Utf-8 -*


from tkinter import *
# Création de la fenêtre principale (main window)
fenetre = Tk()
#titre de la barre au dessus de la fenêtre
fenetre.title('Premier dessin')
#création d'un canvas qui sera une zone pour le dessin
#bg pour la couleur de fond et bd pour la taille de la bordure
#qui sera de la couleur du fond
zone_dessin=Canvas(fenetre,scrollregion=(0,0,500,500),width=500,height=500,border=0)
#affichage de la zone
#ligne droite
zone_dessin.create_line(0,0,50,50,fill="black",width=1)
#rectangle
zone_dessin.create_rectangle(0,0,499,499,width=3,outline="black")
#ovale
zone_dessin.create_oval(150,150,350,350,fill="orange",width=4)
zone_dessin.grid(column=0,row=0)

# lancement de la boucle tkinter
fenetre.mainloop()
