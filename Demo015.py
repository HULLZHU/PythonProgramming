
students= ['zhu','zhu','zhu','Qi',"QiQI","Linziqi"]

new_stu=[student for student in students if len(student)>2]

for i in students:
    print(i)

for i in new_stu:
    print(i)