import math
num = 1
str0 = ""
for i in range(10):
    num = num * 2
    log2n = math.log(num,2)
    n = num
    nlogen = n*math.log(n)
    n2 = num**2
    n3 = num**3
    final = 2 **n
    str0 = str(log2n) + " "+ str(n)+ " "+ str(nlogen) +" "+ str(n2)+" "+str(n3) +" " + str(final) +"\n"
    print(str0)
