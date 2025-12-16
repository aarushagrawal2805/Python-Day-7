# Read line by line a File
try:
    with open("Custom.py", "r") as f:
        for i in range(10):
            print(f.readline().strip())#strip means it remove extra space and newline
except FileNotFoundError:
    print("File not Found")
