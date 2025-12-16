#Create a function that takes a filename as input and returns the total number of words in that file
import re

def count_words(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            words = re.findall(r'\b\w+\b', content) # Use regex to find whole words
            return len(words)
    except FileNotFoundError:
         print("Error:",filename,"not found.")

# Example usage:
word_count = count_words("Custom.py")
print("Total words: ",word_count)