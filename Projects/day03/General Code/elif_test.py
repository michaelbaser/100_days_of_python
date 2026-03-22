print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#----------------
# elif version 1
#----------------

# Instead of having if / else statement
# You can add as many elif conditions as required
print("-------- Elif version 1 --------")

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5$")
    elif age >= 12 and age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
    
    
#----------------
# elif version 2
#----------------

# Instead of having if / else statement
# You can add as many elif conditions as required
print("-------- Elif version 2 --------")
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5$")
    elif age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
    
    
#----------------
# elif version 3
#----------------

# Instead of having if / else statement
# You can add as many elif conditions as required
print("-------- Elif version 3 --------")
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5$")
    elif age > 18:
        print("Please pay 12$")
    else:
        print("Please pay $7")
else:
    print("Sorry you have to grow taller before you can ride.")