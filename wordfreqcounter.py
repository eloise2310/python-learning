# WORD FREQUENCY COUNTER
# create a programme that reads a text file 
# counts the frequency of each word in the file (ignoring case, punctuation etc)
# handles errors gracefylly using exceptions: if the file does exist, print helpful message, if any issues reading the file, handle them and print an error message
# writes the word frequencies to a new file called word_frequencies.txt
# sorts the words into alphabetical order before writing them to the file

import string # importing so we can use string.punctuation to remove punctuation
from collections import Counter # impoting to use collections.Counter which is a class that counts the occurrences of each element in a list

def word_count(alice):
    try:
        with open("alice.txt", "r") as file:
            content = file.read()
            content = content.lower()
            content = content.translate(str.maketrans('', '', string.punctuation)) # removes punctuation 

            words = content.split()

            word_frequency = Counter(words)

            return word_frequency
    
    except FileNotFoundError:
        print(f"Error: The file '{alice}' was not found")
        return {}
    
    except IOError:
        print("Error: There was an issue with reading the file")
        return {}

    else:
        print("File read successfully")
        return {}
    
filename = "alice.txt"

word_frequency = word_count(filename)

if word_frequency:
    print(f"The file contains {sum(word_frequency.values())} words.")
    print("Word frequencies:")

    for word in word_frequency.keys():
        count = word_frequency.get(word)
        print(f"{word}: {count}")

else:
    print("Word count could not be calculated")