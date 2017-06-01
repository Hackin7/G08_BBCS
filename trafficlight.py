from microbit import *
while True:
    reading = pin0.read_analog()
    if reading > 256: pin16.write_digital(1)
    else: pin16.write_digital(0) 
    if reading > 512: pin15.write_digital(1)
    else: pin15.write_digital(0) 
    if reading > 768: pin14.write_digital(1)
    else: pin14.write_digital(0)
