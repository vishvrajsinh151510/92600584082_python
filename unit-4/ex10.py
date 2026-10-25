with open('ex9.txt','r') as f:
    print("-----------\n")
    print("Initial position:", f.tell())
    print("Read data:", f.read(5))
    print("Position after reading:", f.tell())
    f.seek(5)
    print("Position after seek:", f.tell())

    print("Read data again:",f.read(4))
    print("pointer posistion:",f.tell())