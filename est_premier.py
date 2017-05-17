import math
import pickle
#affichage d'une liste
def aff(l):
    for i in range(0,len(l)):
        print(l[i])



def est_premier(n):
    test=True
    #print("n=",n)
    for i in range(2,int(math.sqrt(n+1)+1)):
        #print("i=",i)
        if n%i==0:
            test=False
    return test
        

def l_prem(k):
    l=[]
    for i in range(2,k):
        if est_premier(i):
            l.append(i)
    return l

"""with open('liste_premiers','wb') as fichier:
    liste_premiers=pickle.Pickler(fichier)
    liste_premiers.dump(l_prem(10))

with open('liste_premiers','rb') as fic:
    lp=pickle.Unpickler(fic)
    liste_recupere=lp.load()

print('recup',liste_recupere)

"""

reponse=input("Est-ce la première utilisation du programme ? (oui/non)")
if reponse.lower()=="oui":
    with open('liste_premiers','wb') as fichier:
        liste_premiers=pickle.Pickler(fichier)
        liste_premiers.dump(l_prem(10))

with open('liste_premiers','rb') as fic:
    lp=pickle.Unpickler(fic)
    l_r=lp.load()
print("liste de nombre premier actuelle : ")
print(l_r)
test=True
while test:
    k=int(input("combien de termes en plus ? (0 pour arrèter)"))
    if k==0:
        test=False
    nb_de_nb=0
    cpt=0
    while cpt<k:
        i=l_r[len(l_r)-1]+1
        while not est_premier(i):
            i=i+1
        l_r.append(i)
        cpt=cpt+1
print(l_r)
with open('liste_premiers','wb') as fichier:
    liste_premiers=pickle.Pickler(fichier)
    liste_premiers.dump(l_r)
