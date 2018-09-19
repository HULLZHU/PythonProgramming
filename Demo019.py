longest_name = None
max_letters = 0

names = ["Cecilia",'Lise','Marie']
lens_name = [len(x) for x in names]

for i in range(len(names)):
    count = lens_name[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)

for i,name in enumerate(names):
    count = lens_name[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

