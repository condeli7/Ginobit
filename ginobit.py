from microbit import i2c, pin19, pin20
from time import sleep
import struct

COVER_DISTANCE_W_SPEED = 1	        #   cover a distance of clicks (positive or negative) with set speed
COVER_DISTANCE_W_POWER_PERCENT = 2  #   cover a distance of clicks (positive or negative) with set power percent
SPIN_WITH_SPEED = 3	                #   spin with a set speed of clicks per second (max is around +-60)
SPIN_WITH_POWER_PERCENT = 4	        #   spin with set PWM ratio
STOP = 5	                        #   Break mode
STOP_IDLE = 6	                    #   Idle mode (no break)

PACKET_LENGTH = 13           #   Maximum number of bytes to be received by Ginobot over i2c
GINOBOT_DEV_ID = 22



"""
Ginobot class used to control a Ginobot through Python
"""

class ginobit:

    def __init__(self):

        self.packet_string = [PACKET_LENGTH]
        i2c.init(freq=400000, sda=pin20, scl=pin19)

    @staticmethod
    def command(command):

        i2c.write(GINOBOT_DEV_ID, command)
        sleep(0.050)
        data = i2c.read(GINOBOT_DEV_ID, 13)
        try:
            string = str(data, 'utf-8')
            integer = int(string)
        except ValueError as e:
            integer = -1
            pass

        return integer
