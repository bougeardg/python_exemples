import math

#Exemple de procedure - affichage d'une table de multiplication
def table(nb, max):
    i=0
    while i < max: # Tant que i est strictement inférieure à la variable max,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
table(13,5)


#Exemple de fonction-rapide

f=lambda x:pow(x,3)#x^3

print(f(5))

#Exemple de fonction
def g(x):
    return 5*math.sqrt(x)+3#5*sqrt(x)+3

print(g(3))

#On peut appeler une fonction définie dans un fichier annexe fonctions2.py

from fonctions_annexe import fact
print("6!=",fact(6))


# effets des fonctions/procedures sur les variables extérieures

a=2
print('avant ajou, a=', a)
def ajou(a):
    a=a+2
    print('pendant ajou, a=',a)

ajou(a) # l'appel à ajou plante car $a$ n'est pas définie dans ajou
print('après ajou, a=',a)
#a n'est pas modifié par la procedure/fonction car elle est définie à l'extérieure

def ajou_bis():
    global a #la déclaration de a comme globale permet à la procedure/fonction
    #d'en modifier la valeur à l'extérieur de la procedure
    a=a+2
    print('pendant ajou_bis, a=',a)

ajou_bis()
print('après ajou_bis, a=',a)
#les objets ne sont pas ceoncerné par ce pb, ils sont modifié par les procédures/fonctions
