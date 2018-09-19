import math
import sys
b = 4
c= 3

discriminant = b*b - 4.0*c
d = math.sqrt(discriminant)
print(-b+d/2.0)
print(-b-d/2.0)
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a%b==0)