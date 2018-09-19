import math
epsilon = 1e-15
c = 10
t = 12

count = 0
while t*t - c > abs(epsilon):
    t = c/(2*t)+t/2
    count +=1
    print("Count:"+str(count))
    print(t)