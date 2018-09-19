import sys
import random
import math


a = int(sys.argv[1])
b = int(sys.argv[2])

randomNumber = random.randint(a, b)
print(randomNumber)

a = random.randint(1,7)
b = random.randint(1,7)
print(a+b)

a = int(sys.argv[1])
print(math.sin(2*a) + math.cos(3*a))