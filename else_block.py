#Using else Block

def Value():
 try:
    x=int(input("Enter First Number :"))
    y=int(input("Enter Second Number:"))
    print("Divide is :",x/y) 
 except ValueError:
   print("String Can't BE Divide !")
 else:
   print("Code Executed Succesfully 😁")

Value()