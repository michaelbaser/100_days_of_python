# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#------------
# Packages
#------------

import random


#------------
# Variables
#------------

# Set at_goal to False so it runs
at_goal = False

#------------
# Functions 
#------------

# Build functions for sandbox
def move():
    print("Robot moves forward")

def turn_left():
    print("Robot turns left")

 # Def turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Def jump
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#------------
# Hurdles 2, at_goal != True method
#------------
# if not at goal, continue jumping
  
# Set at_goal to False so it runs
at_goal = False
total_hurdles_to_jump = random.randint(1,10)
number_of_hurdles = 0

print(f'\nHurdles 2 - while loop "!= True"" method:')
while at_goal != True:
    jump()
    
    number_of_hurdles += 1
    print(f'That is hurdle {number_of_hurdles} cleared!')
    
    if number_of_hurdles == total_hurdles_to_jump:
        at_goal = True
        print(f'You made it! There was a total of {total_hurdles_to_jump} hurdles on your path to olympic gold for "at_goal != True"!')
    
    
#------------
# Hurdles 2, not at_goal method
#------------
  
# Reset


# Set at_goal to False so it runs
at_goal = False
total_hurdles_to_jump = random.randint(1,10)
number_of_hurdles = 0
  
print(f'\nHurdles 2 - while loop "not at_goal" method:')
while not at_goal:
    jump()
    
    number_of_hurdles += 1
    print(f'That is hurdle {number_of_hurdles} cleared!')
    
    if number_of_hurdles == total_hurdles_to_jump:
        at_goal = True
        print(f'You made it! There was a total of {total_hurdles_to_jump} hurdles on your path to olympic gold for "not at_goal"!')
    
  


  
  