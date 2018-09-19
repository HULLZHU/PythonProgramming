flavor_list = ['vanilla','chocolate','pecan','strawberry']
for flavor in flavor_list:
    print('My Fruit: %s'%flavor)

for (index,flavor) in enumerate(flavor_list):
    print("My %d Fruit: %s"%(index+1,flavor))


