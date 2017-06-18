# tri d'une liste - quicksort
import random
#création s'une liste 
l=list() #vide
n=1000
for i in range(n):
    l.append(i)
l=random.sample(l,len(l))#mélange
print(l)
def tri(li):#fonction récursive de tri
    if len(li)==0:
        return []
    elif len(li)==1:
        return li
    else:#si la liste est de longueur 2 au moins
        k=random.randrange(0,len(li)) #choix du pivot au hasard
        pivot=li[k]
        """création de deux listes qui seront respectivement
        composées des éléments inf, égaux et  sup au pivot de la liste de départ    """
        linf=list()
        leq=list()
        leq.append(pivot)
        lsup=list()
        #chaque élémént de la liste va dans celle qui lui convient
        for i in range(len(li)):
            if i!=k:
                if li[i]<pivot:
                    linf.append(li[i])
                else:
                    lsup.append(li[i])
        # pour finir on concatène les trois listes.
        return (tri(linf) + leq + tri(lsup))

print(tri(l))
