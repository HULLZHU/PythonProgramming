import random
m = 10
n = 1000
a = []
for i in range(n):
    a = a + [i]
b = []
for i in range(m):
    randomIndex = random.randint(0,1000)
    b += [a[randomIndex]]

print(b)
