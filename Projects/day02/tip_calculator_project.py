print(f"Welcome to the tip calculator!")

bill_input = input("What was the total bill? $")
bill_amount = round(float(bill_input),2)

print(f"How much tip would you like to give? 10, 12 or 15?")
tip_amount = int(input())
tip_amount_for_final = 1 + (tip_amount / 100)

print(f"How many people to split the bill? ", end="")
number_of_people = int(input())

print(f"The bill_amount type is {type(bill_amount)}\n "
      f"The tip_amount type is {type(tip_amount)}\n"
      f"The number_of_people type is {type(number_of_people)}")

bill_calculation = (bill_amount / number_of_people) * tip_amount_for_final

bill_calculation_formatted = round(float(bill_calculation),2)

# The amount they have to pay to 2 decimal places
print(f"Each person should pay: ${bill_calculation_formatted}")