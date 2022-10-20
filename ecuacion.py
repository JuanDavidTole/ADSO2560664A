from math import sqrt

def solucion_ecuacion(a,b,c):
    determinar=b*2-4*a*c

    if determinar >0: 
        x_1=-b + sqrt(b**2-4*a*c) / (2*a)
        x_2=-b - sqrt(b**2-4*a*c) / (2*a)
    return x_1, x_2

    if determinar == 0:
        x_1 = -b /(2*a)
        return(x_1,)
        
    else:
        return tuple()
        


            

    

