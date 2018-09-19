str = ""
for i in range(1,11):
    for j in range(1,11):
        if i % j ==0 or j % i == 0 :
            str = str +" *"
        else:
            str = str + "  "
        if j % 10 == 0:
            str = str+'\n'

print(str)


