import os
import sys

if os.path.exists("new_folder"):
    print("Folder already exists.")
else:
    os.mkdir("new_folder")
    print("Folder created successfully.")

with open("new_folder/new_file.txt",'w') as f:
    f.write("hello everyone!")
    f.write("This is a new file created in the new_folder.\n")
    f.write("i am vishvrajsinh zala .\n")

with open("new_folder/new_file.txt",'r')as f:
    print(f.read())


with open("new_folder/new_file.txt",'a') as f:
    f.write("This is an additional line added to the file.\n")
    f.write("Appending more content to the existing file.\n")
    print("Additional content appended to the file successfully.")


print("Current working directory:", os.getcwd())
print("list of files:", os.listdir('new_folder'))

if os.path.exists("new_folder/new_file.txt"):
    print("File exists.")
    print("File size:", os.path.getsize("new_folder/new_file.txt"), "bytes")
else:
    print("File does not exist.")


print("command line arguments:", sys.argv )
print("Python Version:", sys.version)


# os.remove("new_folder/new_file.txt")
# print("File deleted successfully.")

# os.rmdir("new_folder")
# print("Folder deleted successfully.")