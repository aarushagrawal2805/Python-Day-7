#Exception with Function Arguments

def square(num):
    if not isinstance(num, int): # isinstance check num is int or not 
        raise TypeError("Only integers allowed")
    return num * num

try:
    print(square(5))
    print(square("a"))
except TypeError as e:
    print(e)
