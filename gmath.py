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

    return vector


#Return the dot product of a . b
def dot_product(a, b):
    x0 = a[0]
    y0 = a[1]
    z0 = a[2]

    x1 = b[0]
    y1 = b[1]
    z1 = b[2]

    dp = x0*x1+y0*y1+z0*z1
    return dp

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i+1]
    p2 = polygons[i+2]

    #a = p1-p0, b=p2-p0
    a = [p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2]]
    b = [p2[0]-p0[0], p2[1]-p0[1], p2[2]-p0[2]]

    normal = [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
    return normal
