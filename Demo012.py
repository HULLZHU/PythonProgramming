file = open("C:/Users/yuan/Desktop/DemoForInput.txt")
value = [len(x) for x in file]
print(value)

def generator1(n):
    a= 10
    b= 10
    c= 10
    while(n < a + b + c ):
        yield n
        n +=1

g = generator1(25)
for i in range(29):
    print(next(g))

def generator2(n):
    for i in range(8):
        n = n + "I love you"
        yield n

g2 = generator2("Lin ziqi")

print(next(g2))


