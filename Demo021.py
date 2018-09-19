dict1 = {1:'hello',2:'good',3:'bad'}
dict2 = {4:'wa'}
dict1.update(dict2)
print(dict1)
print(dict1.items())
a = [1,2,3,4]
dict3 = dict1.fromkeys(a)
num = dict1.pop(1)
print(dict3)
print(dict1)
print(num)