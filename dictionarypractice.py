# DICTIONARIES
# create a dictionary for storing information and iterate over it

person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Iterating over the dictionary's keys
for key in person_info:
    value = person_info[key]  # Accessing the value using the key
    print(key.capitalize() + ": " + str(value))
