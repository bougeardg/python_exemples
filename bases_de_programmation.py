#structure conditionnelle
a=5
print('a=',a)
if a >0:
    print('a est positif')
elif a<0 :
    print('a est negatif')
else :
    print('a est \'nul')

#entrée par l'utilisateur
annee=input("saisissez une année : ")#le résultat est une chaine
annee=int(annee)#on peut le convertir en entier
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print(annee, " est bissextile.")
else:
    print(annee," n'est pas bissextile.")


#boucle while

print("calcul de factoriel n")
n=int(input("saisissez un nombre entier "))
i=1
fact=1
while i<n:
    i+=1
    fact=fact*i
print(n,"!=",fact)


#boucle for
fact=1
for i in range(n):
    fact=fact*(i+1)
print(n,"!=",fact)
