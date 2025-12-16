#Custom Exception

def Vote():
 try:
    age = int(input("Enter Your Age :"))
    if age < 18:
        raise Exception ("You are not eligible to vote")
    else:
        print("You are elligible to vote")
 except ValueError:
    print("Invalid Input !")
 except Exception as e:
    print(e)

Vote()