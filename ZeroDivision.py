#Handle Division by Zero
def Divi():
    try:
     a = int(input("Enter First Number :"))
     b = int(input("Enter Second Number :"))
     c=a/b
     print("Divide is :",c)
    except ZeroDivisionError:
     print("Number Cannot Divide By Zero !")

Divi()