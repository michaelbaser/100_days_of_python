
#------------
# Functions 
#------------

# Build functions for sandbox
def move():
    2 > 1

def turn_left():
    2 > 1

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
# Infinite loop test 
#------------


while 5 > 3:
    print(5 > 3)
    jump()
    
