# # creating set
# # myset={"banana","apple","guva"}
# # print(myset)
#
# # Accessing data from set variable
# # myset={"banana","apple","guva"}
# # for i in myset:
# #     print(i)
#
# #Example3 value exist in the set or not
#
# # myset={"banana","apple","guva"}
# #
# # if "apple" in myset:
# #     print("The values is existed")
# # else:
# #     print("the value is not existed")
# # Example4
# # if "yellow" in myset:
# #     print("the value is existed in the list")
# # else:
# #     print("the value is not existed")
#
# # Example5 adding items in to the set
# # myset={"banana","apple","guva"}
# # Using Two function we can handle this.
# # 1)add()
# # 2)update()
# # myset.add("kiwi")
# # print(myset)
# # myset.add("grapes")
# # print(myset)
#
# # 2)update() To add multiple values we can use this.
# # To Add multiple values into the set you can use square brackets.
# # myset={"banana","apple","guva"}
# # myset.update("kiwi","grapes","pine apple")
# # # print(myset)
#
# # myset1={"water","food","sweet"}
# # print(myset1)
# # myset1.update(["tata","steel","ratan"])
# # print(myset1)
#
# #How to find number of items in the set
# myset={"banana","apple","guva"}
# print(len(myset))
# # How to remove items from the set
# myset.remove("banana")
# print(myset)
# # myset.clear()
# print(myset)
#
# # I want to join two sets
# a={1,2,3,4}
# b={"a","b","c"}
# c=a.union(b)
# print(c)
from os import remove

a={1,2,3,4}
c={"f","i"}
a.remove(1)
print(a)
print(a)
# b=a.union(c)
