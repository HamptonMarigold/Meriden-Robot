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

         # MOTOR 1 (is LHS)
         # MOTOR 2 (is RHS)
 
        motor(1,1,400)
        motor(2,1,400)
        sleep(4500) #  
        
        motor(2,1,0)    # only one motor to stop as motor 2 never started
        sleep(1000)     # 1000 - magic time to turn thro' 90 degrees
        
        motor(1,1,400)
        motor(2,1,400)
        sleep(4500)
        motor(1,1,0)
        motor(2,1,0) # stop motors

    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        # not sure if needed ? robot issue?
        motor(1,1,0)
        motor(2,1,0) # stop motors
    else:
        display.show(Image.SAD)
        # not sure if needed ? robot issue?
        motor(1,1,0)
        motor(2,1,0) # stop motors

    