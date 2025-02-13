# physical.py
# physical side of things, like the actual calculator
# screen implementation

import time
import board
import digitalio
import busio
#import matrixFunctions as matrix

# every single button
bm = digitalio.DigitalInOut(board.GP0)
bm.switch_to_input(pull=digitalio.Pull.DOWN)
b0 = digitalio.DigitalInOut(board.GP1)
b0.switch_to_input(pull=digitalio.Pull.DOWN)
b1 = digitalio.DigitalInOut(board.GP2)
b1.switch_to_input(pull=digitalio.Pull.DOWN)
b2 = digitalio.DigitalInOut(board.GP3)
b2.switch_to_input(pull=digitalio.Pull.DOWN)
b3 = digitalio.DigitalInOut(board.GP4)
b3.switch_to_input(pull=digitalio.Pull.DOWN)
b4 = digitalio.DigitalInOut(board.GP21)
b4.switch_to_input(pull=digitalio.Pull.DOWN)
b5 = digitalio.DigitalInOut(board.GP20)
b5.switch_to_input(pull=digitalio.Pull.DOWN)
b6 = digitalio.DigitalInOut(board.GP19)
b6.switch_to_input(pull=digitalio.Pull.DOWN)
b7 = digitalio.DigitalInOut(board.GP18)
b7.switch_to_input(pull=digitalio.Pull.DOWN)
b8 = digitalio.DigitalInOut(board.GP17)
b8.switch_to_input(pull=digitalio.Pull.DOWN)
b9 = digitalio.DigitalInOut(board.GP16)
b9.switch_to_input(pull=digitalio.Pull.DOWN)

# screens -> "busio.I2C(board.GP17, board.GP16)", "busio.I2C(board.GP19, board.GP18)"
i2cA = busio.I2C(board.GP17, board.GP16)
i2cB = busio.I2C(board.GP19, board.GP18)
display_busA = displayio.I2CDisplay(i2cA, device_address=0x3C)
displayA = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display_busB = displayio.I2CDisplay(i2cB, device_address=0x3C)
displayB = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

while (True):
    print("menu >> " + str(bm.value) + " 0 >> " + str(b1.value))
    time.sleep(.25)
