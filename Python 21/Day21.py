import os

input_directory = 'A2'

output_file = 'ALZ.txt'

consolidated_data = ''

for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_directory, filename)
        with open(file_path, 'r') as file:
            file_contents = file.read()
            consolidated_data += file_contents

with open(output_file, 'w') as output:
    output.write(consolidated_data)

print(f"Consolidated data has been written to {output_file}")