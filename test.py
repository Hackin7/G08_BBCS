from microbit import *

#######################################
while True:
  presses = button_a.get_presses()
  display.scroll(str(presses))
  sleep(200)
#######################################
while True: # the microbit is alive
  presses = button_a.get_presses() #
  if presses > 5: 
    display.show(Image.DIAMOND)
  else:
      #w we need to know when we've failed
      display.show(Image.ANGRY)
  sleep(2000)
#######################################  
while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading_x > 20 :
        display.show("L")
    elif reading_x < -20 :
        display.show("R")
    else:
        display.show("-")
#Flappy Bird######################################
#CONSTANTS - very important
#these label your values, allowing your code to be more readable and are normally
#named with 
DELAY = 20
FRAMES_PER_WALL+SHIFT = 20
FRAMES_PER_NEW_WALL = 100
FRAMES_PER_SCORE = 50

# global variables
Y = 50     # the bird's (starting) position along the y axis, between 0-99 inclusive (100 numbers)
speed # this is the speed of your bird ;). There will be a downward acceleration, and downward direction is taken as positive
score  # the player's score
frame = 0  # the game's instances

# only the
