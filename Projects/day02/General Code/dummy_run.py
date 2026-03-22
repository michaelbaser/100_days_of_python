weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

print("Starting with coded run")

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")

print("Starting with user input run")

user_weight = float(input("Please enter your weight "))
user_height = float(input("Please enter your height "))

user_bmi = user_weight / (user_height ** 2)

print(f"Your bmi = {user_bmi}")

if user_bmi < 18.5:
    print("underweight")
elif user_bmi >= 18.5 and user_bmi < 25:
    print("normal weight")
else:
    print("overweight")

