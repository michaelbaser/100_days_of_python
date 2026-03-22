import random
import my_module

random_integer = random.randint(1, 10)
print(f"\nUsing random.randint for random integer 1 to 10 = {random_integer}")

# Pulling from my_module script
print(f"\nMy favourite number = {my_module.my_favourite_number}")

# Return the next random floating-point number in the range 0.0 <= X < 1.0
random_number_0_to_1 = random.random()
print(f"\nUsing random.random float 0 to 1 = {random_number_0_to_1}")

# Return the next random floating-point number in the range 0.0 <= X < 1.0
# Mulitplied by 10
random_number_multiplied = random.random() * 10
print(f"\nUsing random.random float 0 to 1 multiplied by 10 = {random_number_multiplied}")

# Number between a and b, inclusive

# Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
# The end-point value b may or may not be included in the range depending on floating-point rounding in the expression a + (b-a) * random().
random_float = random.uniform(1, 10)
print(f"\nUsing random.uniform 1 to 10 = {random_float}")