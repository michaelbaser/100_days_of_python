# The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. 
# Instead of looping through each item in a List, we can loop through a range of numbers.

# Range Function
# range(1, 10)

# This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.

# But it can be used in conjunction with For Loops. e.g.

# for number in range(1, 10):
#     print(number)
# This will print out each of the numbers 1 - 9. So the range can also be expressed like this:

# a <= range(a, b) < b

# Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.

#------------
# General testing
#------------


# Range function does not do anything by itself e.g. printing this does not print 1 through 10
print(f'Print "range(1,10)" = {range(1,10)}')
# range(1, 10)

print('\n')

# Need to be used in conjunction with another function such as below

# Range as 1, 6
for number in range(1, 6):
    print(f'Results of "range(1, 6)" loop: {number}')
# Results of "range(1, 6)" loop: 1
# Results of "range(1, 6)" loop: 2
# Results of "range(1, 6)" loop: 3
# Results of "range(1, 6)" loop: 4
# Results of "range(1, 6)" loop: 5

print('\n')

# Range as 1, 6 with step by 2:
for number in range(1, 6, 2):
    print(f'Results of "range(1, 6, 3)" loop: {number}')
# Results of "range(1, 6, 3)" loop: 1
# Results of "range(1, 6, 3)" loop: 3
# Results of "range(1, 6, 3)" loop: 5

print('\n')

# Test for 10 as end range, so max of range print = 9
for number in range(1, 10):
    print(f'Results of "range(1, 10)" loop: {number}')
# Results of "range(1, 10)" loop: 1
# Results of "range(1, 10)" loop: 2
# Results of "range(1, 10)" loop: 3
# Results of "range(1, 10)" loop: 4
# Results of "range(1, 10)" loop: 5
# Results of "range(1, 10)" loop: 6
# Results of "range(1, 10)" loop: 7
# Results of "range(1, 10)" loop: 8
# Results of "range(1, 10)" loop: 9

print('\n')

# Test for 11 as end range, so max of range print = 10
for number in range(1, 11):
    print(f'Results of "range(1, 11)" loop: {number}')
# Results of "range(1, 11)" loop: 1
# Results of "range(1, 11)" loop: 2
# Results of "range(1, 11)" loop: 3
# Results of "range(1, 11)" loop: 4
# Results of "range(1, 11)" loop: 5
# Results of "range(1, 11)" loop: 6
# Results of "range(1, 11)" loop: 7
# Results of "range(1, 11)" loop: 8
# Results of "range(1, 11)" loop: 9
# Results of "range(1, 11)" loop: 10

print('\n')

# By default the range will step through all the names from the start to the end with increase by 1
# To increase by number need to specify step-size for example can do by 3
for number in range(1, 11, 3):
    print(f'Results of "range(1, 11, 3)" loop: {number}')
# Results of "range(1, 11, 3)" loop: 1
# Results of "range(1, 11, 3)" loop: 4
# Results of "range(1, 11, 3)" loop: 7
# Results of "range(1, 11, 3)" loop: 10

print('\n')

#------------
# PAUSE 1 - The Gauss Challenge
#------------

# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

sum_var = 0

for number in range(1, 101):
    sum_var += number
    
    
print(f'Using "sum_var" method with for loop range: {sum_var:,}')