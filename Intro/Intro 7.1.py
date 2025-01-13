with open("example.txt", "w") as file:
    file.write("This is a sample text")
with open("example.txt", "r") as file:
    content = file.read()
print(content)
