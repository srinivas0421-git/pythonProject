# list1=[45,2,5,6,7]
# print(set(list1))
# set1=set(list1)
# print(set1)
#
# for i in set1:
#     print(i)
# set2={'name','age','salary'}
# print(set2)
# #joining two or more sets using union
# set3=set1.union(set2)
# print(set3)
# set4={45,2,6,9,10}
# set5=set3.intersection(set4)
# print(set5)
# set5=set3.difference(set4)
# print(set5)

# set6={1,2,3,4,5}
# set7={1,2,3,4,5,66.8,56,89}
# set8=set6.difference(set7)
# print(set8)

# set1={1,2,3,4,5,6,7,8,9,10}
# set1.add(20)
# print(set1)
# set1.update("name","age")
# print(set1)



# set2={1,2,3,4,80,90,100,200}
# set3=set1.difference(set2)
# print(set3)
# set3=set1.intersection(set2)
# print(set3)
# set3=set1.union(set2)
# print(set3)


myset={"apple","mango","grapes","kiwi"}
print(myset)
myset1={"name","age","rollno"}
myset3=(myset.issubset(myset1))
print(myset3)

myset.remove("apple")
print(myset)

myset1.discard("age")
print(myset1)

myset.clear()
print(myset)






