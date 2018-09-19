r = 36.0
g = 129.0
b = 68.0
w = max(r/255,g/255,b/255)
c = (w - (r/255))/w
m = (w - (g/255))/w
y = (w - (b/255))/w
k = 1 - w

str1 = str(c)+ ":"+str(m)+":"+str(k)
print(str1)