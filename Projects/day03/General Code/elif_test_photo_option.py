print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket_price = 0

#__________
# elif
#__________

# Instead of having if / else statement
# You can add as many elif conditions as required

if height >= 120:

    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        ticket_price = 5
        ticket_price_orig = 5
        ticket_category = "child ticket"
        print("Child tickets are 5$")
    elif age >= 12 and age <= 18:
        ticket_price = 7
        ticket_price_orig = 7        
        ticket_category = "young adult ticket"
        print("Young adult tickets are 7$")
    else:
        ticket_price = 12
        ticket_price_orig = 12        
        ticket_category = "adult ticket"
        print("Adult tickets are $12")

    photo_option = input("Would you like a photo? Type 'y' for yes and 'n' for no: \n")

    if photo_option == "y":
         # Add on +3 to ticket_price variable
        ticket_price += 3
        print(f"Your total bill is ${ticket_price}\n"
              f"Breakdown: as you are age {age}, this means you fall within the {ticket_category} category for ${ticket_price_orig}\n"
              f"plus +$3, as you said yes for the photo")
    else:
        print(f"Your total bill is ${ticket_price}\n"
              f"Breakdown: as you are age {age}, this means you fall within the {ticket_category} category for ${ticket_price_orig}\n"
              f"plus no added extras, as you said no for the photo")


else:
    print("Sorry you have to grow taller before you can ride.")