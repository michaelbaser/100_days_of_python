# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


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
# Hurdles 1 
#------------
print("\nHurdles 1 - repeat code method:")
jump()
jump()
jump()
jump()
jump()
jump()

print("\nHurdles 1 - for loop method:")
for hurdle in range(6):
    jump()
    
    
print("\nHurdles 1 - while loop, count up method with break:")
number_of_hurdles = 0
while number_of_hurdles < 6:
  jump()
  if number_of_hurdles == 6:
    break
  number_of_hurdles += 1
  print(number_of_hurdles)


print("\nHurdles 1 - while loop, count up method no break:")
number_of_hurdles = 0
while number_of_hurdles < 6:
  jump()
  number_of_hurdles += 1
  print(number_of_hurdles)

print("\nHurdles 1 - while loop, count down method with break:")
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()
  if number_of_hurdles == 0:
    break
  number_of_hurdles -= 1
  print(number_of_hurdles)
  
  
  
print("\nHurdles 1 - while loop, count down method no break:")
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1
  print(number_of_hurdles)
  
  
print("\nHurdles 1 - while loop, simplified:")
number_of_hurdles = 6
while number_of_hurdles > 0:
  number_of_hurdles -= 1
  print(number_of_hurdles)