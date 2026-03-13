# Program to read a file and handle errors

try:
    # Open the file in read mode
    file = open("sample.txt", "r")

    print("Reading file content:")

    # Read and print file line by line
    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
    

#.......................
 #........................
   #.............................

# Program to write and append data to a file

# Take user input
data = input("Enter some data: ")

# Write data to the file
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Read and display final content
with open("output.txt", "r") as file:
    print("\nFinal content of the file:")

    print(file.read())
