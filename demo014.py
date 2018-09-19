import sys
def generatorLove (n):
    for i in range(8):
        n = n+"I love you"
        yield n

g = generatorLove("LinZiqi ")

while True:
    try:
        print(next(g))
    except:
        sys.exit(1)


n = ['1',2,'3','4',5]
g2 = generatorOfString(n)

while True:
    try:
        print(next(g2))
    except:
        sys.exit(1)