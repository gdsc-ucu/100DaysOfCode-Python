
input_files = ['task.txt', 'list.txt', 'school.txt']

output_file = 'consolidated_data.txt'

try:
    with open(output_file, 'w') as output:
        for input_file in input_files:
            with open(input_file, 'r') as file:
                file_contents = file.read()
                output.write(f"=== Contents of {input_file} ===\n")
                output.write(file_contents)
                output.write("\n\n")
        print(f"Consolidated data saved to {output_file}")

except FileNotFoundError:
    print("One of the input files or the output file was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

