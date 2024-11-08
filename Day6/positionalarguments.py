#Example 1

# def func(i,j):
#     print(i,j)
# func(10,20)
#Example 2
# def func(i,j=20):
#     print(i,j)
# func(10)
#Example3 positional arguments.

# def func(i,j=70):
#     print(i,j)
# func(100,200)
# func(300,400)
# func(500)

# Example4 positional parameters

# def greetings(name,greetmsg):
#     print(name,greetmsg)
# greetings("srinivas","welcome")

# Example5 keyword arguements
# def greetings(greeting,name):
#     print(greeting +" "+ name)
# greetings(greeting="welcome to hyderabad",name="srinivas")
# #Example 6 keyword arguments
#
# def wish(name,salary,location):
#     print("my name"+" "+name+" "+"salary is"+ " "+salary+ " " + " and location is \"+location)
# wish(name="srinivas",salary="50000",location="hyderabad")

#Example6 both positinal and keyword

# def func(a,b,c):
#     print(a,b,c)
# func(10,20,30)
# func(a=20,b=30,c=40)
# func(c=40,a=20,b=90)
#
#  func(10,20,c=40):#10,20,40
#  func(10,e=20,c=40): #10,20,40
#  func(10 d=20,50):#10,20,50

#Function can return multiple values.
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

# larg=largest(20,40)
small=largest(10,5)
# print(larg)
print(small)
print(type(small))







