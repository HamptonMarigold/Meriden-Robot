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
        motor(1,1,400)
        motor(2,1,400)
        sleep(5000)     # (goes fwd for 5 secs)
     
      
        motor(1,1,0)    # after 5000 (5 seconds)  motor 1 stops 
        sleep(4000)     # cicles on spot for 4 secs 
        
        motor(1,1,0)
        motor(2,1,0)    # stop spiining after 4 secs
        sleep(2000)     # stops for 2 secs.... note if did not sleep could 
                        # have just moved from one action to another without sleep or stop
        
        motor(1,1,400)
        motor(2,2,400) # spin motors in opposite directions
        sleep(5000)
        
        motor(1,1,300)
        motor(2,1,600) # circle        
        sleep(10000)
        motor(1,1,0)
        motor(2,1,0) # stop motors
        
        
        
        
    elif button_b.is_pressed():
        display.show(Image.FABULOUS)
        #note sure should really need these next 2 lines, but something dodgy going on
        #one motor runs as soon as connect power to motor and microbit
        motor(1,1,0)
        motor(2,1,0) # stop motors

    else:
        display.show(Image.ASLEEP)
        #note sure should really need these next 2 lines, but something dodgy going on
        motor(1,1,0)
        motor(2,1,0) # stop motors
