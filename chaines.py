#création d'une chaine
str1="ceci est une chaîne"
#chaine vide
str2=""


print(str1)

#mettre en majuscule (la modification n'est pas enregistrée)
print(str1.upper())
print(str1)

#majuscule pour la première lettre
print(str1.capitalize())

#concaténation
str2=str1+". " + str1
print(str2)

str3=""
for i in range(0,15):
    str3=str3+str(i)
    
#Extractions de  sous chaînes
print(str3)

    #intervalle
print(str3[0:7])
print(str3[7:12])

    #premiers et derniers caractères
print(str3[:3])# les 3 premiers
print(str3[-3:])# les 3 derniers
print(str3[3:])# tous sauf les 3 premiers
print(str3[:-3])# Tous sauf les 3 derniers

#parcours d'une chaine
for charac in str1:
    print(charac)

#code ASCII d'un caractère

print('a en décimal',ord('a'))
print('a en hexadécimal',hex(ord('a')))
print('a en binaire',bin(ord('a')))
