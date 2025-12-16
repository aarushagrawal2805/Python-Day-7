#Exception Handling in Function

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error:  Can't Division by zero"

print(divide(10, 2))
print(divide(10, 0))
