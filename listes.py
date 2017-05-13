import math

#affichage d'une liste
def aff_liste(l):
    for i in range(0,len(l)):
        print(l[i])

#Création d'une liste
# Vide
l1=list()
#non vide
l2=[7,8]

#Ajout d'un élément à la fin
l1.append(0)
for i in range(1,5):
    l1.append(i)

n=1
print("test",n)
aff_liste(l1)

#Insertion d'un élément où on veut
l1.insert(4,3.1416)
n=2
print("test",n)
aff_liste(l1)


#concaténation de deux listes
l1.extend(l2)

n=3
print("test",n)
aff_liste(l1)

#supression d'un élément de la liste avec l'indice
del l1[4]

n=4
print("test",n)
aff_liste(l1)

#suppression d'un élément de la liste avec l'élémént
l1.remove(7)
n=5
print("test",n)
aff_liste(l1)
#et s'il y a 2 fois le même, seul le premier rencontré est supprimé
l1.insert(3,6)
l1.insert(5,6)
n=6
print("test",n)
aff_liste(l1)
l1.remove(6)
n=7
print("test",n)
aff_liste(l1)



liste_premiers=[2,3,5,7]

#Fonction qui trouve le nombre premier dans la suite de la liste
def ajout_premier(l):
    n=len(l) #longueur de la liste
    k=l[n-1] #dernier élément de la liste
    trouve=False
    while not trouve:
        k=k+1
        divisible=False
        j=0
        while j<n and not divisible and l[j]<math.sqrt(k):
            if k%l[j]==0:
                divisible=True
            j=j+1
        if not divisible:
            trouve=True
            return k

for i in range(0,5):
    liste_premiers.append(ajout_premier(liste_premiers))
print("liste de nombres premiers")

aff_liste(liste_premiers)



#enregistrement de la liste dans un fichier
import pickle
with open('liste_premiers','wb') as fichier:
    liste_a_sauver=pickle.Pickler(fichier)
    liste_a_sauver.dump(liste_premiers)
#récupération de la liste enregistrée
with open('liste_premiers','rb') as fic:
    l=pickle.Unpickler(fic)
    liste_recupere=l.load()
print("liste récupérée du fichier")
aff_liste(liste_recupere)
liste_premiers=liste_recupere
#Ajout de 5 nombres premiers
for i in range(0,5):
    liste_premiers.append(ajout_premier(liste_premiers))
print("la nouvelle liste")
aff_liste(liste_premiers)
