# # # # #Exanple1
# # # #
# # # # class Bank():
# # # #     def Rateofintrest(self):
# # # #         return 0
# # # # class xBank(Bank):
# # # #     def Rateofintrest(self):
# # # #         return 20
# # # # class yBank(Bank):
# # # #     def Rateofintrest(self):
# # # #         return 30
# # # #
# # # # obj=xBank()
# # # # print(obj.Rateofintrest())
# # # #
# # # # obj=yBank()
# # # # print(obj.Rateofintrest())
# # # #
# # # # obj=Bank()
# # # # print(obj.Rateofintrest())
# # #
# # # #Example 2 using multiple inheritance
# # # class parent1():
# # #     def show(self):
# # #         print("inside part1")
# # # class parent2():
# # #     def display(self):
# # #         print("inside part2")
# # # class chiled(parent1,parent2):
# # #     def show(self):
# # #         print("inside chiled")
# # #
# # #
# # # obj=chiled()
# # # obj.display()
# # # obj.show()
# # #Example 3
# # class calculation1():
# #     def add(self,a,b):
# #         print(a+b)
# # class calculation2(calculation1):
# #     def mul(self,x,y):
# #         print(x*y)
# # class calculation3(calculation2):
# #     def add(self,a,b):
# #         print(a+b)
# # class calculation4(calculation2):
# #     def mul(self,x,y):
# #         print(x*y)
# #
# # obj=calculation2()
# # obj.add(10,20)
# # obj.mul(20,40)
# from Day9.package2.b import birds
#
#
# # Example4
# # class parent():
# #     def display(self):
# #         print("inside parent")
# # class child(parent):
# #     def show(self):
# #         print("inside chiled")
# # class grandchildren(child):
# #     def show(self):
# #         print("inside grand children")
# #
# # obj=grandchildren()
# # obj.show()
# # obj.display()
#
#
#
#
#
# #Example9
# # class A:
# #     def add(self,a,b):
# #         print(a+b)
# # class B(A):
# #     def sub(self,a,b):
# #         print(a-b)
# # class C(B):
# #    def sub(self,a,b):
# #        super().add(self)
# # obj=C()
# # obj.add(10,20)
# # obj.sub(20,40)
#
#
# class GFG1:
#     def __init__(self):
#         print('HEY !!!!!! GfG I am initialised(Class GEG1)')
#
#     def sub_GFG(self, b):
#         print('Printing from class GFG1:', b)
#
#     # class GFG2 inherits the GFG1
#
#
# class GFG2(GFG1):
#     def __init__(self):
#         print('HEY !!!!!! GfG I am initialised(Class GEG2)')
#         super().__init__()
#
#     def sub_GFG(self, b):
#         print('Printing from class GFG2:', b)
#         super().sub_GFG(b + 1)
#
#     # class GFG3 inherits the GFG1 ang GFG2 both
#
#
# class GFG3(GFG2):
#     def __init__(self):
#         print('HEY !!!!!! GfG I am initialised(Class GEG3)')
#         super().__init__()
#
#     def sub_GFG(self, b):
#         print('Printing from class GFG3:', b)
#         super().sub_GFG(b + 1)
#
#     # main function
#
#
# if __name__ == '__main__':
#     # created the object gfg
#     gfg = GFG3()
#
#     # calling the function sub_GFG3() from class GHG3
#     # which inherits both GFG1 and GFG2 classes
#     gfg.sub_GFG(10)

# class grandfather():
#     x=20
#     def home(self):
#         print("old home")
# class father(grandfather):
#     a=10
#     def home(self):
#         print(super().x)
#         print("1bhk")
# class son(father):
#     def home(self):
#         super().home()
#         print(super().a)
#         print("no home")
# obj=son()
# obj.home()

# Example 5
# class shape():
#     def area(self):
#         print("Print the area of the shape")
# class Rectangle():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print(self.length*self.width)
# class circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius
#
# shap1=Rectangle(2,4)
# print(shap1.area())
#
# shap2=circle(10)
# print(shap2.area())
#Example8
class Father():
    a=10
    def home(self):
        print("Father has old house")
class son(Father):
    b=20
    def home(self):
        super().home()
        print(super().a)
        print("1bhk")
class grandson(Father):
    def home(self):
        super().home()
        print(super().a)
        print("4bhk")
obj=grandson()
obj.home().

# obj=son()
# obj.home()
