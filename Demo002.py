n = 123456789
m = 0
while n!=0:
    m = (10*m) + ( n % 10 )
    n /= 10
print(m)