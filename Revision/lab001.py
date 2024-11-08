# # # collection
# # # List Example1
# # # mylist=["Apple","Orange","banana","watermelon","grapes","kiwi","cherry"]
# # # print(mylist) #['Apple', 'Orange', 'banana', 'watermelon', 'grapes', 'kiwi', 'cherry']
# # # print(mylist[1:5]) #['Orange', 'banana', 'watermelon', 'grapes']
# # # print(mylist[-7:-2])# ['Apple', 'Orange', 'banana', 'watermelon', 'grapes']
# # # #add items into list
# # # mylist.append("guva")
# # # print(mylist)
# # # mylist.insert(2,"papaya")
# # # print(mylist)
# # #
# # # for i in mylist:
# # #     print(i)
# #
# # mylist=["Apple","Orange","banana","watermelon","grapes","kiwi","cherry"]
# #
# # # # for i in mylist:
# # # #     print(i)
# # #
# # # if "Apple" in mylist:
# # #     print("Apple is existed in the list")
# # # else:
# # #     print("apple is not existed in the list")
# # #
# # # print(len(mylist))
# # # mylist.pop(2)
# # # print(mylist)
# # #
# # # del mylist[2]
# # #
# # # # print(mylist.clear())
# # #
# # # del mylist[3]
# # # del mylist[-2]
# # # del mylist[-1]
# # # print(mylist)
# #
# # list1=['a','b','c']
# # list2=[1,2,3]
# # # print(list1+list2)
# #
# # list1.extend(list2)
# # # print(list1)
# #
# #
# # for i in list2:
# #     list1.append(i)
# #     print(i)
# #
# # from collections import deque
# # queue=deque(["Eric","John","Michael"])
# # print(queue)
# # queue.append("Terry")
# # print(queue)
# # queue.appendleft()
# #
# # squares=[]
# # for x in range(10):
# #     squares.append(x**2)
# #     print(squares)
#
# # qubes=[]
# # for y in range(10):
# #     qubes.append(y**3)
# #     print(qubes)
#
# # squares = list(map(lambda x: x**2, range(10)))
# # print(squares)
# # squares = [x**2 for x in range(10)]
# # print(squares)
#
# # t=12345,54321,'hello'
# # print(t[0])
# # u=t,[1,2,3,4,5] #here the list can be nested
# # print(u)
#
# # mylist=['a','b','c']
# # mytuple2=tuple(mylist)
# # print(mytuple2)
# #Dictionary
#
# Student_infor={"name":"srinivas",
#                "age":30,
#                "address":"KA"
#                }
# print(Student_infor)
#
# student_infor2={"name":'shanmukh',
#                 "age":4.5,
#                 "address":"kdd"
#                 }
# print(student_infor2)
#
# # for i in student_infor2:
# #     print(i)
# for i in student_infor2:
#         print(i)
from Day5.ditinarycollection import mydict

# mydict1={"brand":"benz","model":2024,"cost":100000000}
# print(mydict1)
#
# for i in mydict1:
#     print(i)

list1=[1,2,3,4,3,5,6]

list2=set(list1)
print(list2)


mylist=["s",'for','m','sr','s','m']
# mylist2=set(mylist)
# print(mylist2)
print(set(mylist))

mylist3=list(mylist)
print(mylist3)

list3=["name","initial","lastname"]
list4=["s",'for ','z']
list5=list3.subList(list4)
print(list5)