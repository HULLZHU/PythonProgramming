names = ["Zhuhe","Linziqi","Shenhongxia","Qiuqiu","Zhubingjun","LaLa"]
letters = [len(x) for x in names]
max_letter = 0
longest_Name = ""
for name,count in zip(names,letters):
    if count > max_letter:
        longest_Name = name
        max_letter = count

print(longest_Name+" "+str(max_letter))
