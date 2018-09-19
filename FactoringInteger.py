n = 18
factor = 2
factors = []
while factor*factor <= n:
    while n % factor == 0:
        n = n/factor
        factors.append(factor)
    factor = factor + 1

print(factors)