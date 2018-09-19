import random
n = 100
count = 0
collectedCount = 0
isCollected = []

#initialize thge isCollected[]
for i in range(n):
    isCollected =isCollected+[False]

while collectedCount < n :
    value = random.randrange(0,n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True

print(count)
