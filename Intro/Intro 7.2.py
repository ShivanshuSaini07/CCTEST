with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")
with open("example.txt", "r") as file:
    updated=file.read()
print(updated)
