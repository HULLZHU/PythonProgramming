import math
x0 = 3
k = 4
c = 9.0
delta = 1e-15

while  x0 -c/math.pow(x0,k-1) > delta:
    upper = c - math.pow(x0,k)
    lower = k * math.pow(x0,k-1)
    x0 = x0 + upper/lower


print(str(x0))
