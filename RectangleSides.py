import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print(a+b>c or a+c>b or b+c>a)