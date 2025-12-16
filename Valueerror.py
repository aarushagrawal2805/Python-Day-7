#Handle Invalid Input (ValueError)

def Value():
 try:
    x=int(input("Enter First Number :"))
    y=int(input("Enter Second Number:"))
    return x/y
 except ValueError:
   print("String Can't BE Divide !")

Value()