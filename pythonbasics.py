# TO RUN A SCRIPT ---> (in terminal) ---> python3 file_name.py

# ASSIGNING A VALUE TO A VARIABLE
x = 5
name = "Alice"
is_active = True

# BASIC STRING OPERATIONS
text = "Hello, World!"
print(text[0])   # 'H' (indexing)
print(text[7:12]) # 'World' (slicing)
print(text.lower()) # 'hello, world!' (method call)
print(text.upper()) # 'HELLO, WORLD!' (method call)

# concatinating 

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # "John Doe"

# escape charaters 

text = "This is a line break:\nNext line"
print(text)


# DATA TYPES
x = 5           # int
y = 3.14        # float
name = "Alice"   # str
is_active = True # bool


# FUNCTIONS
# defining the function

def add_numbers(num1, num2):
    result = num1 + num2
    return result 

# calling the function 

sum_result = add_numbers(5, 7)

# printing the result 

print("The sum is:", sum_result)

# CONDITIONAL STATEMENTS

x = 10
if x > 0:
    print("x is positive")
elif x == 0: 
    print("x is zero")
else: 
    print("x is negative")

# LOOPS

for i in range(5):
    print(i)

# while loop

x = 0
while x < 5:
    print(x)
    x += 1

# LISTS 

fruits = ["apple", "banana", "cherry"]
fruits.append("pinapple") # adds the item to the list
fruits[0] = "orange" # replaces index 0 (apple) with orange
print(fruits[1:3]) # slicing - prints from index 1 up to (but not including) index 3

# DICTIONARIES 
# A dictionary is an unordered collection of key-value pairs. Dictionaries are created using curly braces {}

person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])  # Output: Alice

person["job"] = "Engineer" # adds a new key-value pair

# accessing a value with the get() method:
print(person.get("age"))  # Output: 30

# ERROR HANDLEING 
# Python uses try, except blocks to handle erros 

try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# TUPLES
# tuples are immutable - cannot be modified once created 

# A tuple with integers
my_tuple = (1, 2, 3, 4, 5)

# A tuple with strings
names_tuple = ("Alice", "Bob", "Charlie")

# A tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)

# A tuple with a single element (important to include a comma)
single_element_tuple = (42,)

my_tuple = (10, 20, 30, 40, 50)

# Accessing the first element
print(my_tuple[0])  # Output: 10

# Accessing the last element
print(my_tuple[-1])  # Output: 50

# Slicing a tuple (getting a subset)
print(my_tuple[1:4])  # Output: (20, 30, 40)

# CLASSES

class Robot_dog: # use the 'class' key word followed by the class name
    def __init__(self, name, breed): # the init method lets us initialise our robots - always import self and then any other perameters needed
        self.name = name
        self.breed = breed 
    
    # adding a method 
    def bark(self):
        print("Woof!")

# main programme
my_dog = Robot_dog("Tilly", "Labrador") # enter dogs info
print(my_dog.name)
print(my_dog.breed)

my_dog.bark() # calling the bark method



        
            



