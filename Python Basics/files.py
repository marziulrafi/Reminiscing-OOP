# Open the file in read mode
file = open("test.txt", "r")
print(file.read())  # prints all text
file.close()

# Write mode (overwrites the file)
file = open("test.txt", "w")
file.write("New content here")
file.close()

# Append mode (adds new line without deleting old)
file = open("test.txt", "a")
file.write("\nAppended line")
file.close()







# Using with


# Writing (overwrites)
with open("test.txt", "w") as f:
    f.write("First line\n")

# Appending (adds new content)
with open("test.txt", "a") as f:
    f.write("Second line\n")

# Reading
with open("test.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)
