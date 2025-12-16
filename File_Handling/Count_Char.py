#Count Total Number of Characters in File

def count_character(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            return (len(content))
    except FileNotFoundError:
        print("File not found")

count=count_character("Basic.py")
print("Total Count Of Characters is :",count)