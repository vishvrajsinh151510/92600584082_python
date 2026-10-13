import shutil

with open("demo.txt",'w') as f:
    f.write("this is a demo file for shutil module.\n")
    print("demo.txt file created successfully.")

shutil.copy("demo.txt","demo_copy.txt")
print("demo.txt file copied to demo_copy.txt successfully.")

shutil.move("demo_copy.txt","new_folder/demo_copy.txt")
print("demo_copy.txt file moved to new_folder successfully.")

shutil.copytree("new_folder","new_folder_copy")
print("new_folder copied to new_folder_copy successfully.")

shutil.make_archive("new_folder_archive","zip","new_folder")
print("new_folder archived to new_folder_archive.zip successfully.")

shutil.unpack_archive("new_folder_archive.zip","unpacked_folder","zip")
print("new_folder_archive.zip unpacked to unpacked_folder successfully.")

# shutil.rmtree("new_folder_copy")
# print("new_folder deleted successfully.")


