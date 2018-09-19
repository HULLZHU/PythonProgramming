import Employee
emp1 = Employee.Employee(name = "Zhu",salary = 1000)
emp2 = Employee.Employee(name = 'Lin',salary = 900)
emp3 = Employee.Employee(name ="Qiuqiu",salary = 500)
var = Employee.Employee.getAllEmpInfo()
print(var)

eng1 = Employee.Engineer("zhuHE",1000)
eng2 = Employee.Engineer("Lin",1200)
print(Employee.Engineer.getAllEngInfo())
print(Employee.Employee.getAllEmpInfo())
print(eng1.__str__())