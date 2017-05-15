# recherche des solutions de cos(x)=x dans [0 ; pi/2]
import math
def f(x):
    return math.cos(x)-x

def dicho(a,b,e):
    c=(a+b)/2
    if abs(b-a)<e:
        return c
    else:
        if (f(c)*f(a)<0):
            return dicho(a,c,e)
        else:
            return dicho(c,b,e)

print(dicho(0,2,0.000000001))
        
