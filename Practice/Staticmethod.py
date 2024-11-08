# # # # class Familly():
# # # #     def srinivas(self,name):
# # # #         print("Head of the familly is :",name)
# # # #     def bhavani(self,name,name1):
# # # #         print(name,"is the mother of my children")
# # # #     def shanmukh(self,name):
# # # #         print("what is the father name of shanmukh:",name)
# # # #     def lohitha(self,name):
# # # #         print("what is the father name of lohitha:",name)
# # # #     @staticmethod
# # # #     def m2(self,num):
# # # #         print(num)
# # # #     @staticmethod
# # # #     def m1(self,name):
# # # #         print(name)
# # # #
# # # # obj=Familly()
# # # # obj.srinivas("srinivas")
# # # # obj.bhavani("shanmukh","Lohitha")
# # # # obj.lohitha("srinivas")
# # # # obj.shanmukh("srinivas")
# # # # # Familly.m1(1,"SRINIVAS")
# # # # Familly.m2(100,200)
# # # # Familly.m1("srinivas","shanmukh")
# # # #
# # # #Example 1
# # # # Constructor
# # # class Myclass():
# # #     def __init__(self):
# # #         print("this is a constructor")
# # #     def m1(self):
# # #         print("hello")
# # #     def m3(self,x,y):
# # #         return x+y
# # #
# # # obj=Myclass()
# # # obj.m1()
# # # bb=obj.m3(10,20)
# # # print(bb)
# # # print(obj.m3(80,40))
# # # cc=obj.m3(60,40)
# # # print(cc)
# #
# # #Example 2
# # class cons():
# #     def __init__(self,ename,eid,esal):
# #         self.ename=ename
# #         self.eid=eid
# #         self.esal=esal
# #     def display(self):
# #         print(self.ename,self.eid,self.esal)
# # obj=cons("srinivas",120,20000)
# # obj.display()
# # obj1=cons("shanmukh",121,4000)
# # obj1.display()
# # ------------------------------------------------------------------------
# # single&multi level level inheritance:
# #
# # class A:
# #     def m1(self):
# #         print("this is a class a ")
# # class B(A):
# #     def m2(self):
# #         print("this is class B")
# # class C(B):
# #     def m3(self):
# #         print("this is class c")
# # obj=C()
# # obj.m1()
# # obj.m2()
# # obj.m3()
# # ----------------------------------------------------
# class A:
#     a,b=20,40
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=20,50
#     def m2(self):
#         print(self.y-self.x)
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
#
#
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()
# -----
#Heirarchy inheritance

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a+self.b)
# class B(A):
#     super()
#     def sub(self):
#         x,y=20,40
#         print(x-y)
# i,j=20,40
# globals()[i]=20
# globals()[j]=40
# class C(A):
#     def mul(self):
#         print(globals()[i]*globals()[j])
#
# obj=C(20,50)
# obj.display()
# obj.mul()

#Example 5

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a+self.b)
class B:
    def sub(self):
        x,y=20,40
        print(x-y)
i,j=20,40
globals()[i]=20
globals()[j]=40
class C(A,B):
    def mul(self):
        print(globals()[i]*globals()[j])

obj=C(10,20)
obj.display()
obj.mul()
obj.sub()