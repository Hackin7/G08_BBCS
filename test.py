from microbit import *

while True:
  presses = button_a.get_presses()
  display.scroll(str(presses))
  sleep(200)

while True: # the microbit is alive
  presses = button_a.get_presses() #
  if presses > 5: 
    display.show(Image.DIAMOND)
  else:
      #w we need to know when we've failed
      display.show(Image.ANGRY)
  sleep(2000)
  
while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading > 20 :
        display.show("L")
    elif reading < -20 :
        display.show("R")
    else:
        display.show("-")
