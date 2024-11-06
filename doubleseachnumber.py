# DOUBLES EACH NUMBER 
# write a programme that loops through a list and doubles each number 

numbers_list = [1, 2, 3, 4, 5]
doubled_numbers = [] # assign new empty list

for number in numbers_list:
    doubled_numbers.append(number*2) # append adds the new doubled numbers into the empty doubled_numbers list

print("Original numbers:", numbers_list)
print("Doubled numbers:", doubled_numbers)



