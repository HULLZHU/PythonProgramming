import random

random_bits = 0
for i in range(64):
    if random.randint(0,1):
        random_bits |= 1 << i
print(random_bits)