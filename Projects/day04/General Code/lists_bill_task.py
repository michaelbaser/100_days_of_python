import random

# Figure out how to pick a random name from the list of friends.
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print("Let's find out the ever lucky friend to pay the bill!")
#-------------
# Method 1: random choice
#-------------

random_choice = random.choice(friends)

print(f"Using random.choice = {random_choice}")

#-------------
# Method 2: random integer
#-------------

random_int = random.randint(0, 4)

print(f"Using random.randint = {friends[random_int]}")

