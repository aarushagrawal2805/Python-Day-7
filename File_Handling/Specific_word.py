import re
count=0
def count_word(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content)
            return words.count(word)
    except FileNotFoundError:
        print("Error: File not found")
        return 0


# Example usage
filename = "Custom.py"
word = "age"

count = count_word(filename, word)
print("The Word",word,"Occurs",count,"Times")
