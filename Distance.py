import math

def getDistanceToOrigin2D( x = 1, y = 1):
    return math.sqrt(x*x + y*y)

def getDistanceToOrigin3D( x = 1, y = 1, z = 1):
    return math.sqrt(x*x + y*y + z*z)

def getDistanceToOriginMulDim ( *args):
    distanceSquare = 0
    for i in args:
        distanceSquare =distanceSquare + i*i
    return math.sqrt(distanceSquare)

print (getDistanceToOriginMulDim(1,2,3,4,5))
print (getDistanceToOriginMulDim(1,1))
print (getDistanceToOrigin2D(1,1))
