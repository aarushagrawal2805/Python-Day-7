#Handle Key Error in Dictionary

def dict1():
 try:
    dict={
        "name":"Anil",
        "Age":20
    }
    print(dict["marks"])
 except:
   print("Key Error !")

dict1()