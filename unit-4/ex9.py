with open("ex9.txt",'w') as f:
    f.write("i am zala\n")
    f.write("i do the unit 4 exercise\n")
    print("data write in file sucessfully")

with open("ex9.txt",'r') as f:
    print(f.read())

with open("ex9.txt",'a') as f:
    f.write("now i append This data in to the file!")
    print("append sucessfully")

