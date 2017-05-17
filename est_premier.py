import math
import pickle
#affichage d'une liste
def aff(l):
    for i in range(0,len(l)):
        print(l[i])





def est_premier(n,l):
    """ teste si un entier est premier en le testant
    avec les diviseurs de la liste l qui sont sensé être premiers"""
    test=True
    i=0
    while l[i]<math.sqrt(n)and i<len(l):
        #print("i=",i)
        if n%l[i]==0:
            test=False
        i=i+1
    return test
               

def l_prem(k):
    l=[]
    for i in range(2,k):
        if est_premier(i,[2,3]):
            l.append(i)
    return l


reponse=input("Est-ce la première utilisation du programme ? (oui/non)")
if reponse.lower()=="oui":
    with open('liste_premiers','wb') as fichier:
        liste_premiers=pickle.Pickler(fichier)
        liste_premiers.dump(l_prem(10))

with open('liste_premiers','rb') as fic:#chargement depuis le fichier
    lp=pickle.Unpickler(fic)
    l_r=lp.load()

print("liste de nombre premier actuelle : ")
print(l_r)

test=True
while test:# c'est parti pour l'agrandissement de la liste !
    k=int(input("combien de termes en plus ? (0 pour arrêter)"))
    if k==0:
        test=False
    nb_de_nb=0
    cpt=0
    while cpt<k:
        i=l_r[len(l_r)-1]+1
        while not est_premier(i,l_r):
            i=i+1
        l_r.append(i)
        cpt=cpt+1
#affichage-enregistrement de la liste finale
print(l_r)
with open('liste_premiers','wb') as fichier:
    liste_premiers=pickle.Pickler(fichier)
    liste_premiers.dump(l_r)
