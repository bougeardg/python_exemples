import math
def disc(a,b,c):
    return b**2-4*a*c

a=int(input("coefficient de x^2 ? "))
b=int(input("coefficient de x ? "))
c=int(input("coefficient constant ?"))



if a!=0:
    #recherche des racines réelles
    d=disc(a,b,c)
    print("discriminant de ", a, "x^2+",b,"x+", c, "= ",d)
    if d>0:
        print("le polynôme a deux racines :")
        e=(-b-math.sqrt(d))/(2*a)
        f=(-b+ math.sqrt(d))/(2*a)
        print(e, " et ",f)
    elif d==0:
        print("le polynôme a une racine :")
        e=-b/(2*a)
        print(e)
    else :
        print("le polynôme n'a aucune racine réelle")
    # Variations
    g=-b/(2*a)
    h=a*g**2+b*g+c
    if a>0:
        print("la fonction polynôme admet un minimum en",g)
        print("il vaut ", h)
    else:
        print("la fonction polynôme admet un maximums en",g)
        print("il vaut ", h)        
else:
    print("ceci n'est pas un polynôme du second degré")

