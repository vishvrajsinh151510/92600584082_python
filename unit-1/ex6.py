# 6. Write a program to illustrate the use of tuples and sets with basic operations.

#-------------tupal---------------
a=(1,2,3,4,5,6,7,8,9,10,5)

#index
print("First element:",a[0])
print("last element :",a[-1])

#Slicing
print("First 3 elements:", a[:3])
print("Last 3 elements :", a[-3:])

#Length
print("Length of tupal :",len(a))

#count
print("number repeted by",a.count(5),"Times")

#Index
print("the index of number:",a.index(5))

#Membership Operation
print("5 is in tupal   :",5 in a)
print("100 is in tupal :",100 not in a)

#Concatenation
t=(10,20,30)
b=t+a
print("Concatenation:",b)

#repetistion
print("repetition:",t*2)


#Tuple Unpacking
x,y,*z=a
p,q,r=t

print("x=",x,"y=",y,"\nz=",z)
print("p=",p,"q=",q,"r=",r)

#Tuple Packing
tp=10,20,30
print("auto create tupal",tp,"type:",type(tp))

#Single-element Tuple
a=(7,)
print(a,"type:",type(a))

print("\n")
#---------set----------------

print("--------set----------------\n")
s={10,20,30,40,50,60,70}
print("set:",s,"\ntype=",type(s))

#add
s.add(80)
print("Add              :",s)

#Update   add multipal element
s.update([90,100])
print("update           :",s)

#remove
s.remove(100)
print("after remove     :",s)

#pop 
s.pop()
print("any element remove:",s)

print("\n")
s1={10,20,30,40,50}
s2={60,70,40,20,25}
print(s1)
print(s2)
print("\n")

#Union 
print("UNION        :",s1 | s2)

#Intersection
print("Intersection :",s1&s2)

#Difference 
print("Difference   :",s1-s2)
print("Difference   :",s2-s1)

#Symmetric Difference
print("Symmetric Difference:",s1^s2)

#Membership
print(20 in s1)