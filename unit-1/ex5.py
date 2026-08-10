# 5.Write a program to create and manipulate lists using indexing slicing and list comprehensions.
a=[10,20,30,40,50,60,70,80,90,100]

print("first element:",a[0])
print("last element:",a[-1])
print("4th element:",a[3])

#list slicing
print("\n")
print("first 5 elements:\n\t",a[0:5])
print("3 elements:\n\t",a[:3:])
print("last 5 elements:\n\t",a[-5:])
print("Reverse list:\n\t",a[::-1])
print("Alternate elements in reverse:\n\t",a[:1:-2])
print("First 3 elements in reverse:\n\t",a[2::-1])
a[9]=95
print("After updating last element:\n\t",a)

# List Manipulation
print("\n")
a.append(110)
print("append:",a)

a.insert(1,15)
print("insert:",a)

a.remove(15)
print("remove:",a)

print("\n")


#List Comprehension
b=[1,2,3,4,5,6,7,8,9,10]

sq=[i*i for i in b]
print("squares of list b:",sq)

even=[i for i in b  if i%2==0]
print("EVEN             :",even)

c=['apple','banana',2,3,5,6,7]
print("mix list         :",c)
print("data type of list:",type(c))
for i in c:
    print(i*2)    

print("\n")


#connect 2 lists
list1=[4,3,2,8]
list2=[1,5,6,7]
list3=list1+list2
print("connect 2 list   :",list3)

#list extend
list1.extend(list2)
print("Extend           :",list1)

#pop 
list3.pop(2)
print("Pop              :",list3)

#short the list
list3.sort()
print("sorted list3     :",list3)

#reverse the list
list3.reverse()
print("reverse of list3 :",list3)

#length of list
print("length of list3  :",len(list3))

#copy the list
list2=list1.copy()
print("copy list        :",list2)

#finding element in list
print("Index of 5 in list3:",list3.index(5))




#list3.clear()
#print("clear:",list3)


