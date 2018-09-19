n = 10
i = 1
while  i < n + 1:
    j = 1
    str0 = ""
    while j < n+1:
        if ( i % j == 0) or (j % i ==0 ):
            str0 = str0 + "* "
        else:
            str0 = str0 +"  "
        j +=1
    print(str0)


    i +=1

