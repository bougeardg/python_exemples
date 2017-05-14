import math
def disc(a,b,c):
    return b**2-4*a*c

a=int(input("coefficient de x^2 ? "))
b=int(input("coefficient de x ? "))
c=int(input("coefficient constant ?"))
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
    print(" le polynôme n'a aucune racine réelle")
