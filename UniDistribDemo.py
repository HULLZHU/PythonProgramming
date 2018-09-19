import  random
total = 0
trials = 5
max = 0
min = 0
for i in range(trials):
    num = random.random()
    if ( i == 0):
        max = num
        min = num
    if num > max:
        max = num
    elif num < min:
        min = num

    total += num
    average = total / trials

print("The max num is "+ str(max))
print("The min num is "+ str(min))
print("The average num is "+str(average))

