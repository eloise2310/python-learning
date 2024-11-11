# phonebook file to use for pytest testing 

class Phonebook:
    def __init__(self):
        self.numbers = {}
    
    def add(self, name, number): # this function lets us add someone new to the phonebook
        self.numbers[name] = number

    def lookup(self, name): # this function lets us look up someone by name 
        if name not in self.numbers:
            raise KeyError(f"Name {name} not found")
        return self.numbers[name]
    
    def all_names(self):
        return set(self.numbers.keys())
    
    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue 
                if number1 == number2:
                    return False
        return True 
    
