with open("example.txt", "r") as file:
    line_count = sum(1 for _ in file)
print(line_count)
