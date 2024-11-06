# ADVANCED DATA STRUCTURES 
# sets / frozensets / nested data structures 

# SETS 
# A set is a built-in data type in Python that represents an unordered collection of unique elements. Sets are mutable, which means you can add or remove items from them. They are useful when you need to store values that must be unique, and you don’t care about the order in which they are stored

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (combine elements from both sets)
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (get common elements)
intersection_set = set1 & set2
print(intersection_set)  # Output: {3, 4}

# Difference (get elements in set1 but not in set2)
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Symmetric Difference (elements in either set but not both)
symmetric_diff_set = set1 ^ set2
print(symmetric_diff_set)  # Output: {1, 2, 5, 6}

# FROZEN SETS
# frozen sets are immutable versions of sets, suitable for use as dictionary keys or in places where immutability is required

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# Union
print(fs1 | fs2)  # Output: frozenset({1, 2, 3, 4, 5})

# Intersection
print(fs1 & fs2)  # Output: frozenset({3})

# NESTED DATA STRUCTURES
# nested data structures, like lists of lists, dictionaries of lists, and lists of dictionaries, allow you to organize and structure data in a more complex way, which is useful for representing real-world problems (e.g., matrices, employee records, etc.)

# list of lists (2D matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6

# dictionary of lists
students = {
    'John': [90, 85, 88],
    'Sara': [92, 80, 95],
    'Mike': [78, 84, 89]
}
print(students['John'])  # Output: [90, 85, 88]

# list of dictionaries
employees = [
    {'name': 'Alice', 'age': 30, 'department': 'HR'},
    {'name': 'Bob', 'age': 25, 'department': 'IT'},
    {'name': 'Charlie', 'age': 35, 'department': 'Finance'}
]
print(employees[1]['name'])  # Output: Bob
