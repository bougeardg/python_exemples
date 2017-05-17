import math

class Complexe: # nombre complexe
    """classe définissant un nombre complexe
    les opérations associées sont toutes en flottants"""
    def __init__(self,a,b):#constructeur
        self.a=a
        self.b=b
    def module(self):#module
        return math.sqrt(self.a**2+self.b**2)
    def argument(self):#argument
        if self.a>0:
            return math.atan(self.b/self.a)
        elif self.a<0:
            return math.atan(self.b/self.a)+math.pi
        else:
            if self.b>0:
                return math.pi/2
            elif self.b<0:
                return (-1)*math.pi/2
            else:
                return NaN
            
    def add(self,z):#addition
 
        return Complexe(self.a+z.a,self.b+z.b)
    def mult(self,z):#multiplication
        return Complexe(self.a*z.a-self.b*z.b,self.a*z.b+self.b*z.a)
    def conj(self):#conjugué
        return Complexe(self.b,(-1)*self.b)
    def divis(self,z):#division
        denom=z.a**2+z.b**2
        num=self.mult(z.conj())
    def aff(self):#chaine de caractère pour l'affichage
        if self.a != 0:
            tmp=str(self.a)
        else:
            tmp=""
        if self.b<0:
            tmp=tmp+str(self.b)+"i"
        elif self.b==0:
            tmp=tmp
        else:
            if self.a !=0:
                tmp=tmp+"+"
            tmp=tmp+str(self.b)+"i"
        return tmp


#liste de nombres complexes pour tester
   
liste_z=[Complexe(0,3),Complexe(4,0),Complexe(2,2),Complexe(-2,2),Complexe(-2,-2),Complexe(2,-2)]
#tests
for z in liste_z:
    print("z = ",z.aff(),"module : ",z.module(),"argument : ",z.argument())

liste_z[2].add(liste_z[1]).aff()
