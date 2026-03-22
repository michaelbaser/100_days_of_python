print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill_result = 0
size_bill = 0
pep_bill = 0
cheese_bill = 0
valid_size = True

# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.

# todo: work put how much they need to pay based on size choice

if size not in ["S", "M", "L"]:
    valid_size = False
    print("Please enter a valid pizza size (S, M, or L).")

else:
    if size == "S":
        size_bill += 15
        bill_result += 15
        if pepperoni == "Y":
            pep_bill += 2
            bill_result += 2
        if extra_cheese == "Y":
            cheese_bill += 1
            bill_result += 1

    elif size == "M":
        size_bill += 20
        bill_result += 20
        if pepperoni == "Y":
            pep_bill += 3
            bill_result += 3
        if extra_cheese == "Y":
            cheese_bill += 1
            bill_result += 1

    elif size == "L":
        size_bill += 25
        bill_result += 25
        if pepperoni == "Y":
            pep_bill += 3
            bill_result += 3
        if extra_cheese == "Y":
            cheese_bill += 1
            bill_result += 1

# todo: work out how much to add to their bill based on pepperoni choice

# todo: work out final amount based on whether they want extra cheese


if valid_size:
    print(f"Your final bill is: ${bill_result}.")
