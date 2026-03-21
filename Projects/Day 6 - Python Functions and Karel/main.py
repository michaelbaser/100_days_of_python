
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

import random

# Reeborg function style

def move():
    print("Robot moves forward")

def turn_left():
    print("Robot turns left")

step_counter = 0
max_steps = 5

def at_goal():
    global step_counter
    if step_counter >= max_steps:
        print("At goal!")
        return True
    return False

def right_is_clear():
    print("Checking if right is clear")
    return False  # change to True/False to simulate behavior

def front_is_clear():
    global step_counter
    print("Checking if front is clear")
    step_counter += 1
    return True  # change to simulate walls

def wall_in_front():
    return not front_is_clear()

# Build functions for sandbox
def move():
    print("Robot moves forward")

def turn_left():
    print("Robot turns left")
    
    
# Def turn_right:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Follow right-edge of maze

#--------------------------------------
# Main solution
#--------------------------------------
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        

#--------------------------------------       
# Detailed code with solution for not getting stuck in a loop on problem worlds:
#--------------------------------------
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()        
#--------------------------------------

