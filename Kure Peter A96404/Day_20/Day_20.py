# File management
# importing libraries
import os
import shutil

"""Dealing with files"""

# creating files
fileName='File 1.txt'
with open(fileName,'w') as file:
    file.write(">This is a new file.")
print("> New file created: ",fileName)

# renaming files
newFileName="File 2.txt"

# Check if the newFileName already exists, and delete it if it does
if os.path.exists(newFileName):
    os.remove(newFileName)

os.rename(fileName, newFileName)
print("> Renamed to: ",newFileName)

# deleting files
os.remove(newFileName)
print("> Deleted file: ",newFileName)


"""Dealing with folders"""

# creating directories
directory = r'New Folder 1'
if not os.path.exists(directory):
    os.makedirs(directory)
print("> Created direcory ",directory)   
 
# renaming directories
newDirectory='New Folder 2'
os.rename(directory, newDirectory)
print("> Renamed directory: ",newDirectory)

# deleting directories
shutil.rmtree(newDirectory)
print("> Deleted directory: ",newDirectory)
