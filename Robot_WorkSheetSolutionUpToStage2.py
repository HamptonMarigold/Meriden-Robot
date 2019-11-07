# Add your Python code here. E.g.
from microbit import *

def motor(mtr, dir, speed):
    if mtr == 1 :
        if dir == 1 :
            pin8.write_analog(speed)
            pin12.write_analog(0)
        if dir == 2 :
            pin8.write_analog(0)
            pin12.write_analog(speed)
    if mtr == 2 :
        if dir == 1 :
            pin0.write_analog(speed)
            pin16.write_analog(0)
        if dir == 2 :
            pin0.write_analog(0)
            pin16.write_analog(speed)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        motor(1,1,0)
        motor(2,1,0)

    elif button_b.is_pressed():
        display.show(Image.FABULOUS)  
         # these first three lines make sure when we ‘plug in’ the motors are stopped for 6 seconds
        motor(1,1,0) 		# (1 = motor 1, 1 direction, 0 speed)
        motor(2,1,0) 		# (1 = motor 2, 1 ……. 
        sleep (6000)		#6000 milliseconds = 6 seconds
        # now we tell both motors to move for 15 seconds, 
        motor(1,1,400)		# (1 = motor 1, 1  direction, 400 speed)
        motor(2,1,400)
        sleep (15000)		#15 seconds
        # now we stop the motors
        motor(1,1,0)
        motor(2,1,0) # stop motors

    else:
        display.show(Image.SAD)
        #this ensures the motors do not run at start
        motor(1,1,0)
        motor(2,1,0) # stop motors
