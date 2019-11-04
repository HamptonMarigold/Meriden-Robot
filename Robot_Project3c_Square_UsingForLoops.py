from microbit import *

#


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
 
       for i in range(4):
        motor(1,1,400)
        motor(2,1,400)
        sleep(3500) #  forward for 3.5 secs
        
        motor(2,1,0)    # only one motor to stop as motor 2 never started
        sleep(1000)     # 1000 - 1100 - magic time to turn thro' 90 degrees
        
        
        #WHAT IS REAL INTERESTING WITH THIS IS THAT IT DOES NOT NEED A STOP
        #motor(1,1,400)
        #motor(2,1,400)
        #sleep(4500)
        #motor(1,1,0)
        #motor(2,1,0) # stop motors





    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        #    not sure if needed ? robot 
        motor(1,1,0)
        motor(2,1,0) # stop motors
    else:
        display.show(Image.SAD)
        # not sure if needed - Jon says it is
        motor(1,1,0)
        motor(2,1,0) # stop motors

    