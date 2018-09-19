v = 1
n = 10
while v <= n//2:
    v = v*2

while v > 0 :
    if n < v :
        print(0)
    else:
        print(1)
        n -=v
    v//=2

    