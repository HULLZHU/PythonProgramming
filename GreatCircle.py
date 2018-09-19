import math
x1 = 50
y1 = 50
x2 = 80
y2 = 90

d = 60*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(math.radians(y1-y2)))
print(d)