import random
c = []

for i in range(5):
    num = random.uniform(0,5)
    c.append(num)

print(max(c))
print(min(c))