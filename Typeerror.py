#Handle Type Error

def Add(x,y):
  try:
    print("Addition is :",x+y)
  except TypeError:
    print("Type Mismatch !")

Add(1,2)#type(int,int)
Add(0.1,2)#type(float,int)
Add("Add",2)#type(str,int) type error