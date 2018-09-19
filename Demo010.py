def is_Even(nums):
    return nums%2==0

a = filter(is_Even,[1,2,3,4,5,6,7,8])

print(list(a))

b = map(lambda x,y:x+y,[1,2,3,4],[1,2,3,4])
print(b)

def square(n):
    return n**2

c = map(square,[1,2,3,4])
print(list(c))

c= map(lambda x : x**2,[1,2,3,4])
print(list(c))

d = lambda x,y:x+y,[1,2,3,4],[1,2,3,4]
print(d)
print(list(d))

e = map(lambda x : x**2,[1,2,3,4])
print(e)

f = lambda x,y,z:x+y,'hello','boy'
print(f)

g = lambda x,y,z:x+y+z,[1,2,3],[1,2,3],[1,2,3]
print(g)
print(list(g))