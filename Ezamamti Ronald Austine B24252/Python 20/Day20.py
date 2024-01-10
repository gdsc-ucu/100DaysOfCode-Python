import os

#Create a file
file_name = "Apps.txt"
with open(file_name, 'w')as file:
    file.write("This is a new file.")
print("Created file:", file_name)
  
# Delete a file  
os.remove(file_name)
print("Deleted file:", file_name)

# Rename a file
new_file_name = "Groups.txt"
os.rename(file_name, new_file_name)
print("Renamed to:", new_file_name)