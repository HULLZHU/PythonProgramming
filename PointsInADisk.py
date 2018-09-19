import random
import math
innerRadius = 2
outterRadius =3
x=10
y=10
pointNumber = 0
while pointNumber ==0:
    x = 6*random.random()-3
    y = 6*random.random()- 3
    print(str(x*x))
    print(str(y*y))
    print("distance: "+ str(math.sqrt(x*x+y*y)))
    if outterRadius >= math.sqrt(x*x+y*y) >= innerRadius:
        pointNumber = pointNumber + 1
coordinates = (x,y)
print(coordinates)