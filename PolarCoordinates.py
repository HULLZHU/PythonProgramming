import math
def getPolarCoordinates(x= 1, y = 1):
    radians = math.atan2(y,x)
    radius = math.sqrt(x*x + y *y)
    c= (radians,radius)
    return c

print(getPolarCoordinates(1,1))
