# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#------------
# Functions
#------------


# Build functions for sandbox
def move():
    print("Robot moves forward")

def turn_left():
    print("Robot turns left")

# Def turn around
def turn_around():
    turn_left()
    turn_left()

 # Def turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#------------
# Robot rock
#------------
print("\nRobot rock:")
move()
move()
turn_around()
move()
move()
turn_around()
turn_right()
# Robot moves forward
# Robot moves forward
# Robot turns left
# Robot turns left
# Robot moves forward
# Robot moves forward
# Robot turns left
# Robot turns left


#------------
# Square turnaround
#------------
print("\nSquare turnaround:")
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

