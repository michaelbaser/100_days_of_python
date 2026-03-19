# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

# Demo
# https://appbrewery.github.io/python-day4-demo/

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock,paper,scissors]

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

cpu = random.randint(0, 2)

print(f"You chose:\n{rock_paper_scissors[player_input]}\nComputer chose:\n{rock_paper_scissors[cpu]}")

# invalid input
if player_input > 2 or player_input < 0:
    "You typed an invalid number, you lose!"

# draw results
elif player_input == cpu:
    print(f"It's a draw =\\")
    
# rock beating scissors
elif player_input == 0 and cpu == 2:
    print(f"You win! :)")

elif player_input == 2 and cpu == 0:
    print(f"You lose :(")

# scissors beating paper
elif player_input == 2 and cpu == 1:
    print(f"You win! :)")

elif player_input == 1 and cpu == 2:
    print(f"You lose :(")
    
# rock beating paper
elif player_input == 1 and cpu == 0:
    print(f"You win! :)")

elif player_input == 0 and cpu == 1:
    print(f"You lose :(")
