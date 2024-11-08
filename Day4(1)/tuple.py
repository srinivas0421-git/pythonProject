# mytuple=("a", "b", "c", "d", "e")
# print(mytuple)
# print(mytuple[0])
# print(mytuple[2:4])
# print(mytuple[-5:-1])
#
# mylist=list(mytuple)
# print(mylist)
# mylist[0]='z'
# mylist[1]='y'
# print(mylist)
# mytuple1=tuple(mylist)
# print(mytuple1)
#
# Example5 reading tuple using loop
# mytuple=("a", "b", "c", "d", "e")
# print(mytuple)
# for i in mytuple:
#     print(i)

#Check item is existed in the tuple or not

# if "b" in mytuple:
#     print("present")
# else:
#     print("not")
#counting the items in the tuple
# mytuple=("a", "b", "c", "d", "e")
# print(len(mytuple))

#Adding items into the tuple
# Note:in tuple we can add,modify delete,remove items from tuple

#Example copy tuple
# mytuple=("a", "b", "c", "d", "e")
# mytuple1=mytuple
# print(mytuple1)

# removing item from tuple
# mytuple1=("a", "b", "c", "d", "e")
# print(mytuple1)

# Example joining/combining tuple
t1=("a","b","c")
t2=("a","b","c")
t3=t1+t2
print(t3)
# compare two tuples
if t1==t2:
    print("equal")
else:
    print("not equal")



