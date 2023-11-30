


import os
# Create a file
file_name = "new_file.txt"
with open(file_name, 'w') as file:
    file.write(input("Enter file content: "))
    print("Created file:", file_name)

file_name2 = "new_file2.txt"
with open(file_name2, 'w') as file:
    file.write(input("Enter file content: "))
    print("Created file:", file_name2)

# Delete a file
os.remove(file_name)
print("Deleted file:", file_name)

# Rename a file

new_file_name = "renamed_file.txt"
os.rename(file_name2, new_file_name)
print("Renamed",file_name2,"to:", new_file_name)
