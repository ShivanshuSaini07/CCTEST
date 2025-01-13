try:
    num=int(input("Enter the numerator:"))
    denom=int(input("Enter the denominator:"))
    result=num/denom
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero not allowed")
