#Read a File
try:
   with open("Typeerror.py",'r') as file:
    data = file.read()
    print(data)
except FileNotFoundError: 
 print("File not Found")