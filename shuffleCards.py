import random
a = [1,31,4,321,321,31,31,31,31]

for i in range(len(a)) :
    r = random.randint(0,9)
    temp = a[r]
    a[r] = a[i]
    a[i] = r

print(a
      )