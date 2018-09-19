import sys
import math
a = 1
b = 3
c = 1
delta = b*b - 4 * a * c

if  delta < 0 :
    print("A should noy be 0")
    sys.exit(1)
else:
    if delta == 0:
        root = -b/(2*a)
        print("Only One Root")
        print("The root is " + str(root))
    else:
        root1 = (-b + math.sqrt(delta))/(2*a)
        root2 = (-b - math.sqrt(delta))/(2*a)
        print("2 roots exist")
        print("root1:"+ str(root1))
        print("root2:"+ str(root2))

