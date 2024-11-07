# WORD COUNTER 
# write a programme that reads a file, counts the words, and handles potential errors

import string # importing so we can use string.punctuation to remove punctuation

file = open("alice.txt", "r")

def word_count(alice):
    try:
        with open(alice, "r") as file:
            content = file.read()

            content = content.lower() # puts to lower case
            content = content.translate(str.maketrans("", "", string.punctuation)) # removes punctuation

            words = content.split() # splits the content into words

            word_count = len(words)

            return word_count
        
    except FileNotFoundError:
        print(f"Error: The file '{alice}' was not found")

    except IOError:
        print("Error: There was an issue with reading the file")

    else:
        print("File read successfully")

filename = "alice.txt"

word_count = word_count(filename)

if word_count:
    print(f"The file contains {word_count} words")

