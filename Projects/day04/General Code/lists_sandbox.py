import random

# Fruits list
fruits = ["Cherry", "Apple", "Pear"]

print(f"Fruit 0 from list ('Cherry'!) = {fruits[0]}")
print(f"Fruit 1 from list ('Apple'!) = {fruits[1]}")
print(f"Fruit 2 from list ('Pear'!) = {fruits[2]}")

print(f"Fruit -3 from list ('Cherry'!) = {fruits[-3]}")
print(f"Fruit -2 from list ('Apple'!) = {fruits[-2]}")
print(f"Fruit -1 from list ('Pear'!) = {fruits[-1]}")


# Adding an item using append
fruits.append("Avocado")

print(f"\nFruit 3 from list ('Avocado'!) = {fruits[3]}")
print(f"Fruit -4 from list ('Avocado'!) = {fruits[-4]}")
print(f"Fruit -3 from list ('Cherry'!) = {fruits[-3]}")
print(f"Fruit -2 from list ('Apple'!) = {fruits[-2]}")
print(f"Fruit -1 from list ('Pear'!) = {fruits[-1]}")


# Extending - this adds extra items
vegetables = ["Peas", "Carrot"]
fruits.extend(vegetables)

print(f"Fruits with veg added = {fruits}")

# States of america list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", 
                     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", 
                     "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
                     "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]



# Print index numbers specified
print(f"\nState 0 from list = {states_of_america[0]}")
print(f"State 49 from list = {states_of_america[49]}")

# Print random state
random_state_int = random.randint(0,49)
print(f"Random state from list = {states_of_america[random_state_int]}")

# Alter first item (the stationery capital!)
print(f"\nState 1 from list = {states_of_america[1]}")
states_of_america[1] = "Pencilvania" 
print(f"State 1 from list after update = {states_of_america[1]}")

# Adding an item using append
states_of_america.append("Michaeland")

print(states_of_america[50])

# Extending
states_of_america.extend(["Croft Mansion", "Mario Kart World"])

print(states_of_america)


# Check length
print(len(states_of_america))

# Print item 49
print(states_of_america[49])
# Hawaii

# !!! This is an error !!!
# Print item 50, error test
# print(states_of_america[50]) 
# IndexError: list index out of range

# Get the number
num_of_states = len(states_of_america) # 50

# !!! This is an error !!!
# If we run code as below it errors
# print(states_of_america[num_of_states])
# IndexError: list index out of range1

# So when indexing from the number, need to minus 1 for the indexing, as starts counting from 0
print(states_of_america[num_of_states - 1])
