# -$- coding:Utf-8 -*
from tkinter import *
import math
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

def pix_comp(x,y,l,h,x0,y0,xmin,ymin,xmax,ymax):
    z=Complexe(0,0)
    z.a=((x-x0)/l)*(xmax-xmin)
    z.b=((y0-y)/l)*(ymax-ymin)
    return z


def test(z):
    global   eps
    global k
    i=0
    z0=Complexe(0,0)
    while (z0.module()<eps)and(i<k):
        z0=(z0.mult(z0)).add(z)
        i=i+1
    if i==k:
        return True
    else:
        return False
    
def testbis(z):
    if (z.a*z.b)<1:
        return True
    else:
        return False
    
class Complexe: # nombre complexe
    """classe définissant un nombre complexe
    les opérations associées sont toutes en flottants"""
    def __init__(self,a,b):#constructeur
        self.a=a
        self.b=b
    def module(self):#module
        return math.sqrt(self.a**2+self.b**2)
    def argument(self):#argument
        if self.a>0:
            return math.atan(self.b/self.a)
        elif self.a<0:
            return math.atan(self.b/self.a)+math.pi
        else:
            if self.b>0:
                return math.pi/2
            elif self.b<0:
                return (-1)*math.pi/2
            else:
                return NaN
            
    def add(self,z):#addition
 
        return Complexe(self.a+z.a,self.b+z.b)
    def mult(self,z):#multiplication
        return Complexe(self.a*z.a-self.b*z.b,self.a*z.b+self.b*z.a)
    def conj(self):#conjugué
        return Complexe(self.b,(-1)*self.b)
    def divis(self,z):#division
        denom=z.a**2+z.b**2
        num=self.mult(z.conj())
    def aff(self):#chaine de caractère pour l'affichage
        if self.a != 0:
            tmp=str(self.a)
        else:
            tmp=""
        if self.b<0:
            tmp=tmp+str(self.b)+"i"
        elif self.b==0:
            tmp=tmp
        else:
            if self.a !=0:
                tmp=tmp+"+"
            tmp=tmp+str(self.b)+"i"
        return tmp

# Création de la fenêtre principale (main window)
k=25 # nombre iterations
eps=1.5 # précision de bornage
xmin=-1.5
ymin=-1
xmax=1
ymax=1
fact=400
largeur=int((xmax-xmin)*fact)
hauteur=int((ymax-ymin)*fact)
x0=int(abs(xmin)*fact)
y0=int(abs(ymin)*fact)

fenetre = Tk()
#titre de la barre au dessus de la fenêtre
fenetre.title('Premier dessin')
#création d'un canvas qui sera une zone pour le dessin
#bg pour la couleur de fond et bd pour la taille de la bordure
#qui sera de la couleur du fond
zone_dessin=Canvas(fenetre,scrollregion=(0,0,largeur,hauteur),
                   width=largeur,height=hauteur,border=0,
                   bg="white")
#affichage de la zone
for x in range(0,largeur-1):
    for y in range(0,hauteur-1):
        if test(pix_comp(x,y,largeur,hauteur,x0,y0,xmin,ymin,xmax,ymax)):
            zone_dessin.create_line(x,y,x+1,y)
zone_dessin.pack()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
# lancement de la boucle tkinter
fenetre.mainloop()
