from typing import Dict, Any


class Employee(object):
    __empCount = 0
    names_salaries: Dict[Any, Any] = {}

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.names_salaries[name] = salary
        self.__empCount += 1

    def setSalary(self, newSalary):
        self.salary = newSalary

    def getSalary(self, getSalary):
        return self.salary

    def getEmpCount(self):
        return self.empCount

    def fireEmployee(self, instance):
        try:
            if isinstance(instance, str):
                del Employee.names_salarie[instance]
            elif isinstance(instance, int):
                del Employee.names_salaries[instance]
            elif isinstance(instance, list):
                for name in list:
                    del Employee.names_salaries[name]
            Employee.__empCount__ -= 1
        except:
            raise Exception("Please enter a valid name or names")

    def goBankrupt(self):
        Employee.names_salaries.clear()
        Employee.__empCount__ = 0

    @staticmethod
    def getAllEmpInfo():
        return Employee.names_salaries

class Engineer(Employee):
    __names_salaries_Engineer: Dict[Any, Any] = {}
    __engineerCount = 0

    def __init__(self,name,salary):
        super()
        Engineer.names_salaries[name] = salary
        Engineer.__engineerCount +=1


    def __str__(self):
        return "This is a subclass of Employee"

    @staticmethod
    def getAllEngInfo():
        return Engineer.__names_salaries_Engineer