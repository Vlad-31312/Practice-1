with open("sample.txt", "w") as file:
    file.write("Hello\n")
    file.write("This is a sample file.\n")
    file.write("File handling in Python.\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)