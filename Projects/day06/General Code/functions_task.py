def get_user_name():
    name = input("What is your name?\n")
    print("Hello, " + name)
    # Inside the function
#Outside the function

print("Hello")


get_user_name() # calling the function

# Hello
# What is your name? Michael
# Hello, Michael


def get_user_age():
    age = int(input('What is your age?\n'))
    print(f'Hello. You are {age} years old, absolutely fabulous!')

get_user_age()
