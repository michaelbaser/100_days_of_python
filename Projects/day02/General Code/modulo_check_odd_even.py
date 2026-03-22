# Write some code using what you have learnt about the modulo operator
# and conditional checks in Python
# to check if the number in the input area is odd or even.
#
# If it's odd print out the word "Odd" otherwise printout "Even"

# Remember: When modulo a number by 2, if 0 then an even number, if 1 then an odd number

user_number = int(input("Please enter your number: \n"))

result = user_number % 2

if result == 0:
    print(f"Your number of `{user_number}` is an even number! Even Stevens!")
else:
    print(f"Your number of `{user_number}` is an odd number! Peculiar and spooky happenings are afoot!")
