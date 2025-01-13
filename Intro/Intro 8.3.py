try:
    file=open("example.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Execution completed")
