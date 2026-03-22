
# Loops allow us to tell the computer to repeat actions without having to write repeated code.
# If we wanted the computer to print out 1 through to 100,
# it would very painful to type a print statement for every number,
# or even just typing out all the numbers 1 through to 100.
# Loops allow us to create a rule and the computer can follow it to do a repeated action.


# PAUSE 1 - Be a Computer
# Predict what will be printed from the code below:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    
# Apple
# Apple pie
# Peach
# Peach pie
# Pear
# Pear pie


# If not indented, will show up once for the final print(fruits) statement, asking to print the whole list
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)
# Apple
# Apple pie
# Peach
# Peach pie
# Pear
# Pear pie
# Apple
# Apple pie
# Peach
# Peach pie
# Pear
# Pear pie
# ['Apple', 'Peach', 'Pear']