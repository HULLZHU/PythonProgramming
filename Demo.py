import sys
G = 10
x = int(sys.argv[1])
v = int(sys.argv[2])
t = int(sys.argv[3])

print(x + v*t - G*t*t/2)