# tri d'une liste - quicksort
import random
l=list()
n=200
for i in range(n):
    l.append(i)
l=random.sample(l,len(l))

def tri(li):
    if len(li)==0:
        return []
    elif len(li)==1:
        return li
    else:    
        k=random.randrange(0,len(li))
        pivot=li[k]
    
        linf=list()
        leq=list()
        leq.append(pivot)
        lsup=list()
        for i in range(len(li)):
            if i!=k:
                if li[i]<pivot:
                    linf.append(li[i])
                else:
                    lsup.append(li[i])
        return (tri(linf) + leq + tri(lsup))

print(tri(l))
