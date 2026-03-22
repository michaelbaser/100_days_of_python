
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

#------------
# Packages
#------------

import random


#------------
# Fake Reeborg functions
#------------

# We pretend the goal is 10 "steps" away
distance_to_goal = 10
steps_taken = 0

def at_goal():
    """Returns True if we have reached the distance limit."""
    return steps_taken >= distance_to_goal

def wall_in_front():
    """Randomly decides if there is a wall (30% chance)."""
    # In a real script, we don't want a wall at the very last step/goal
    if at_goal():
        return False
    return random.choice([True, False, False]) # False is more likely

def front_is_clear():
    """The opposite of wall_in_front."""
    return not wall_in_front()
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
    
# Def mini jump
def mini_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


#------------
# Hurdles 3, else method
#------------

while not at_goal():
    if wall_in_front():
        jump
    else:
        move()