def divide(a, b):
    try:
        result= a / b
        return result 
    expect ZeroDivisionError:
        return "Error: cannot divide by zero."

print(divide(10, 2))
print(divide(10, 0))