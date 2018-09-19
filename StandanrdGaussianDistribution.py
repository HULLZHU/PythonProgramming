import math
import random

v = random.random()
u = random.random()
print("v : " + str(v))
print("u : " + str(u))

w = math.sin(2 * math.pi * v)*(-2*math.log(u))**0.5

print("result" + str(w))
