# File handling and data structures

inputFiles = ['names.txt','tasks.txt','items.txt']

# Reading data
data = []

for file_name in inputFiles:
    with open(file_name, 'r') as file:
        content=file.read()
        data.append(content)

# Consolidating the data
consolidatedData = '\n' .join(data)

# Writing the output to a file
outputFile='finalOutput.txt'

with open('finalOutput.txt', 'w') as file:
    file.write(consolidatedData)
    
print(f'Consolidated data written to {outputFile}')