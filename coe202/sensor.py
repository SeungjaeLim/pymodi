import modi
import time
"""
Example script for the usage of ir module
Make sure you connect 1 ir module to your network module
"""

if __name__ == "__main__":
    bundle = modi.MODI(conn_type = 'ble',
        network_uuid='6B9F29CB')
    motors = [bundle.motors[0], bundle.motors[1]]
    irs = [bundle.irs[0], bundle.irs[1]]
    button = bundle.buttons[0]
    mode = 0
    course = 0
    threshold_l = 30
    threshold_r = 30
    while True:
        print("{0:<10}{1:<10}".format(irs[0].proximity, irs[1].proximity))
        if button.pressed:
            if mode == 0:
                mode = 1
            else:
                mode = 0
        if mode == 1:
            if irs[0].proximity < threshold_l:
                print("left")
                motors[0].speed = 100, -100
                motors[1].speed = -100, 100
                time.sleep(0.7)
                motors[0].speed = 100, 100
                motors[1].speed = 100, 100
                time.sleep(2)
                motors[0].speed = 100, -100
                motors[1].speed = -100, 100
                
            elif irs[1].proximity < threshold_r:
                print("right")
                motors[0].speed = 100, -100
                motors[1].speed = -100, 100
                time.sleep(0.7)
                motors[0].speed = -100, -100
                motors[1].speed = -100, -100
                time.sleep(2)
                motors[0].speed = 100, -100
                motors[1].speed = -100, 100
            else:
                motors[0].speed = 100, -100
                motors[1].speed = -100, 100
            #if irs[0].proximity > 10:
            #elif: 
            
