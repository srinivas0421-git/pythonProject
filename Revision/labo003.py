#Creating dictinary
from os import remove

mydict={"brand":"toyota","model":1067,"year":2023}
print(mydict)

for i in mydict:
    print(i)

print(mydict["brand"])#toyota
print(mydict["model"])#1067
print(mydict["year"])#2023

mydict["color"]="green"
print(mydict)

print(mydict.get("color"))
mydict["year"]=2022
print(mydict)
mydict["model"]="rolls roy"
print(mydict)

mydict["brand"]="avenger"
mydict["model"]="MDL2025678"
mydict["year"]="2025"
print(mydict)

print("brand" in mydict)

if "brand" in mydict:
    print("the value is existed in the mydict")
else:
    print("the value is not existed in the mydict")

print(len(mydict))
mydict["branch"]="kdd"
print(mydict)
mydict["manager"]="srinivas"
print(mydict)

mydict.pop("color")
print(mydict)
mydict.pop("manager")
print(mydict)

mydict1=mydict
print(mydict1)
mydict2=mydict1.copy()
print(mydict2)

