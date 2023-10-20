
import os

print("Current working directory:", os.getcwd())

# # Read and display data from a text file
# os.chdir("C:\Users\user\Documents\GitHub\100DaysOfCode-Python2\TirzahAtwiine")


file_name =input("Enter name of the file: ")

with open(file_name, 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)