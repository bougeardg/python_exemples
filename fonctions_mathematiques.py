#fonctions de base
print('5+7=',5+7)
print('5*7=',5*7)
print('5/7=',5/7)
print('7%5=',7%5)#reste de 7 module 5
print('-7%5=',-7%5)
print('5^4=', pow(5,4))
print('5^4=', 5**4)


import math
#fonctions trigonométriques
#En radian

print(math.pi)
#en pi/4
print(math.cos(math.pi/4))
print(math.sin(math.pi/4))
print(math.tan(math.pi/4))

#logarithme népérien
print('ln(5)=',math.log(5,math.e))
#exponentiel
print('exp(4)=',math.exp(4))
#racine carrée
print('sqrt(9)=', math.sqrt(9))

#Aléatoire
import random
#tirage aléatoire
print('entre 0 et 1 : ',random.random())
print('entier entre 0 et 5 : ',random.randrange(6))
liste=['riri', 'fifi', 'loulou']
print('un castor junior au hasard :',random.choice(liste))
#12 entiers entre 0 et 19
liste=random.sample(range(20),12)
print('12 entiers entre 0 et 19 : ',liste)
#désordonner une liste
liste=random.sample(range(20),20)
print('de 0 à 19 dans le désordre :',liste)
