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

if size == "S":
    bill_result += 15
    size_bill += 15
if size == "M":
    bill_result += 20
    size_bill += 20
if size == "L":
    bill_result += 25
    size_bill += 15
else:
    print("Please enter a valid size")


# todo: work out how much to add to their bill based on pepperoni choice

if pepperoni == "Y":
    if size == "S":
        bill_result += 2
        pep_bill += 2
    else:
        bill_result += 3
        pep_bill += 2
else:
    print("Please enter a valid option for pepperoni")



# todo: work out final amount based on whether they want extra cheese

if extra_cheese == "Y":
    bill_result += 1
    cheese_bill += 1
elif extra_cheese != "N":
    print("Please enter a valid option for extra cheese")
    


print(f"\n\nYou have ordered a '{size}' size pizza which costs ${size_bill}.\n"
      f"You said '{pepperoni}' to pepperoni which is an additional ${pep_bill}.\n"
      f"You said '{extra_cheese}' to extra cheese which is an additional ${cheese_bill}.\n"          
      f"\nYour final bill is: ${bill_result}")