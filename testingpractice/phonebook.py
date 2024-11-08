# phonebook file to use for unit testing 

class Phonebook:
    def __init__(self):
        self.numbers = {}
    
    def add(self, name, number): # this function lets us add someone new to the phonebook
        self.numbers[name] = number

    def lookup(self, name): # this function lets us look up someone by name 
        return self.numbers[name]
    
    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue 
                if number1 == number2:
                    return False
        return True 