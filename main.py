# from curio import sleep
# from bricknil import attach, start
# from bricknil.hub import PoweredUpHub
# from bricknil.sensor import TrainMotor
import logging
from pylgbst import *
from pylgbst.hub import MoveHub

# @attach(TrainMotor, name='motor')
# class Train(PoweredUpHub):

#     async def run(self):
#         for i in range(2):  # Repeat this control two times
#             await self.motor.ramp_speed(80,5000) # Ramp speed to 80 over 5 seconds
#             await sleep(6)
#             await self.motor.ramp_speed(0,1000)  # Brake to 0 over 1 second
#             await sleep(2)

# async def system():
#     train = Train('cargo_train')
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    conn=get_connection_auto()
    try:
        movehub = MoveHub(conn)
        print("dsffds")
    finally:  
        conn.disconnect()      
    #start(system)