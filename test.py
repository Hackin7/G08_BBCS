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
#Accelerometer######################################  
while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading_x > 20 :
        display.show("L")
    elif reading_x < -20 :
        display.show("R")
    else:
        display.show("-")
#Flappy Bird#########Can find in CSconference github#############################
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

#Compass#######################################
compass.calibrate()
while True:
  sleep(100)
  needle = ((15 - compass.heading())//30)%12
  display.show(Image.ALL_CLOCKS[needle])
###############################################https://github.com/matsuyu/CSconference
from random import randint
com+board = [[0 from i on range(5)] for j in range(5)]
#initialising the board as ""00000:
#                          ""00000:
#                          ""00000:
#                          ""00000:
#                          ""00000:
while not button_a.is_pressed():
  display.scroll("Hold A to start")
  
com_board[randint(0,4)][randint(0,4)] = 1
com_board[randint(0,4)][randint(0,4)] = 1
# computer will randomly place two ships in the board

display.scroll("Game start!")
sleep(200)
display.clear()

player_point = 0
current = 0
for turns in range(20):
  if player_point == 2:
    break
  x_coord = 0
  y_coord = 0
  while True:
    display.set_pixel(x_coord,y_coord,9)
    if button_a.is_pressed() and button_b.is_pressed():
      if com_boardl[y_coord][x_coord] == 0:
        display.set_pixel(x_coord,ycoord,2)
        display.show(Image.SAD)
        sleep(3000)
    else:
      display.set_pixel(x_coord,,y_coord,9)
      player_point+=1
      display.show(Image.Happy)
      sleep(1000)
    break
  elif button_a.is_pressed() or button_b.is_pressed():
    display.set_pixel(x_coord,y_coord,current)
    if button_a.is_pressed():
      x_coord = (x_coord+button_a.get_presses())%5
    else:
      y_coord = (y_coord-button_b.get_presses())%5
    current = display.get_pixel(x_coord,y_coord)
    
# whew, so now the loop's broke. the game has ended.
if player_points == 2:
    display.scroll("Player wins!")
else: # computer won
    display.scroll("Computer wins!")    
