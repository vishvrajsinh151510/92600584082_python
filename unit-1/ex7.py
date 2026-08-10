#7.. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

dict={"name":"vishvrajsinh","age":21,"course":"MCA","marks":75.55,"gread":"a"}
print(dict)

#Accessing Dictionary Elements
print("NAME :",dict["name"])
print("MARKS:",dict["marks"])

#Add New Element
dict["clg"]="Marwadi"
print("after adding element:\n",dict)

#update
dict["age"]=21

print("\n")
#methods
print("Keys     :",dict.keys())
print("Value    :",dict.values())
print("item     :",dict.items())
print("get clg  :",dict.get("clg","Not found"))
dict.pop("gread")
print("after pop:",dict)
dict.popitem()
print("after pop:",dict)

#copy
dict2=dict.copy()
print("copy:",dict2)

#setdefult - add
dict.setdefault("clg","Marwadi")
print(dict)

#Iteration
for i in dict:
    print(i,":",dict[i])

#Iterating through keys
print("\n--Keys--:")
for i in dict.keys():
    print(i)

#Iterating through values
print("\n--values--:")
for i in dict.values():
    print(i)

#Iterating through items
print("\n--Key-Value Pairs--:")
for i,j in dict.items():
    print(i,":",j) 