import random


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]


# Print list 0 (fruits)
print(dirty_dozen[0])
# ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']

# Print list 0 (fruits) and index item 0 from this list
print(dirty_dozen[0][0])
# Strawberries

# Print list 0 (fruits) and index item 1 from this list
print(dirty_dozen[0][1])
# Nectarines

# Print list 1 (vegetables)
print(dirty_dozen[1])
# ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

# Print list 1 (vegetables) and index item 2 from this list
print(dirty_dozen[1][2])
# Tomatoes

# Print list 1 (vegetables) and index item 3 from this list
print(dirty_dozen[1][3])
# Celery