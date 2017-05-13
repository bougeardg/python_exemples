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
