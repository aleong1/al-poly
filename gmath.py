import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = math.sqrt(x*x+y*y+z*z)

    vector[0] = x/mag
    vector[1] = y/mag
    vector[2] = z/mag
    

#Return the dot product of a . b
def dot_product(a, b):
    x0 = a[0]
    y0 = a[1]
    z0 = a[2]
    magA = math.sqrt(x0*x0+y0*y0+z0*z0)

    x1 = a[0]
    y1 = a[1]
    z1 = a[2]
    magB = math.sqrt(x1*x1+y1*y1+z1*z1)

    dp = magA * magB * math.cos()
    
    return dp

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    if i == 0:
        a = polygons[i+1]
        b = polygons[len(polygons)]
    elif i == len(polygons):
        a = polygons[i-1]
        b = polygons[0]
    else:
        a = polygons[i-1]
        b = polygons[i+1]

    

    return None
