

# List of input file names
input_files = ["test1.txt", "test2.txt", "test3.txt"]

# Output file name
output_file = "combined.txt"

# Open the output file in write mode
with open(output_file, "w") as output:
    # Iterate through the list of input file names
    for input_file in input_files:
        # Open each input file in read mode
        with open(input_file, "r") as input:
            # Read the content of the input file
            file_content = input.read()
            
            # Write the content to the output file
            output.write(file_content)

print("Combination complete. Data from", len(input_files), "files has been written to", output_file)
