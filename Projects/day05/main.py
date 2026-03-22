letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

#-----------------
# Easy version - MB answer
#-----------------

print('\n')
#Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$*924

# You can see that all the letters are together. 
# All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

# Random selections
selected_letters = random.choices(letters, k=nr_letters)

selected_symbols = random.choices(symbols, k=nr_symbols)

selected_numbers = random.choices(numbers, k=nr_numbers)



# Concat list
easy_password_list = selected_letters + selected_symbols + selected_numbers

# String list
easy_password = ''.join(easy_password_list)

# Print easy password
print(f'Your (easy) password is: {easy_password}')

#-----------------
# Hard version - MB answer
#-----------------

# When you've completed the easy version, you're ready to tackle the hard version. 
# In the advanced version of this project the final password does not follow a pattern. 

# So the example above might look like this:

# x$d24g*f9

# And every time you generate a password, the positions of the symbols, numbers, and letters are different. 
# This will make the password more difficult for hackers to crack.

# The essential skill of a good programmer is using Google to find what you need. 
# Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. 
# If you get stuck, check the hint below for what to Google.

# Hard password = randomise

# Take a copy of easy list
hard_password_list = easy_password_list[:]

# Shuffle
random.shuffle(hard_password_list)

# String
hard_password = ''.join(hard_password_list)

# Print hard password
print(f'Your (hard) password is: {hard_password}')




#-----------------
# Easy version - course answer 
#-----------------

print(f'\n')
password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_symbols):
    password += random.choice(numbers)


print(f'Your (easy) password (using course method) is: {password}')


#-----------------
# Hard version - course answer
#-----------------


password_list = []

for char in range(0, nr_letters):
    password_list += random.choice(letters)
    
    # alt code using append which has same result:
    # password_list.append(random.choice(letters))
    

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)
    
    # alt code using append which has same result:
    # password_list.append(random.choice(symbols))
    

for char in range(0, nr_symbols):
    password_list += random.choice(numbers)
    
    # alt code using append which has same result:    
    # password_list.append(random.choice(symbols))
    
print(f'Your (hard) password (using course method) ***pre-shuffle list*** is: {password_list}')
# random shuffle on password
random.shuffle(password_list)

print(f'Your (hard) password (using course method) ***post-shuffle list*** is: {password_list}')


password = ""
for char in password_list:
    password += char

print(f'Your (hard) password (using course method) is: {password}')

