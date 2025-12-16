#Multiple Exceptions


def Value():
 try:
    x=int(input("Enter First Number :"))
    y=int(input("Enter Second Number:"))
    print("Division is :",x/y) 
 except ValueError:
   print("String Can't BE Divide !")
 except ZeroDivisionError:
   print("Number Can't Divide By Zero !")

Value()