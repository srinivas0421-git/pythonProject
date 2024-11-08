# from collections.abc import async_generator
# from operator import truediv
# from pickle import FALSE
#
#
# #
# # class person:
# #     def __init__(self,name,id):
# #         self.name=name
# #         self.id=id
# #     def display(self):
# #         print(self.name,self.id)
# # class Emp(person):
# #     def print(self):
# #         print("Emp class called")
# #
# # obj=Emp("srinivas",30)
# # obj.display()
# # obj.print()
#
# #Example 3
#
# class person():
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def isEmployee(self):
#         return FALSE
# class Emp(person):
#     def isEmployee(self):
#         return True
# obj=Emp("srinivas")
# print(obj.getName(),obj.isEmployee())
#
# obj1=Emp("shanmukh")
# print(obj1.getName(),obj1.isEmployee())

#Example4

# class person():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def display(self):
#      print(self.name,self.id)
# class Employee(person):
#     def __init__(self,name,id,salary,post):
#         self.salary=salary
#         self.post=post
#         person.__init__(self,name,id)
#
# a=Employee("shanmukh",120,80000,"developer")
# a.display()
# Example 5

class A:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

class B(A):
    def __init__(self, name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(self.roll)
obj=B("SRI",20)
obj.display()
obj.show()

# Example 6



