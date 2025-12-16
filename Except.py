#Catch All Exceptions

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except Exception as e: # It catch all error in code without defining it fucntion
    print("Error:", e)
