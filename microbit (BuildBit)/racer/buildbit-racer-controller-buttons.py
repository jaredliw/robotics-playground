from microbit import *
import radio
import ghandle

radio.on()
while True:
    if ghandle.B1_is_pressed():
        display.show(Image.ARROW_W)
        radio.send("100 255")
    elif ghandle.B2_is_pressed():
        display.show(Image.ARROW_N)
        radio.send("255 255")
    elif ghandle.B3_is_pressed():
        display.show(Image.ARROW_S)
        radio.send("-255 -255")
    elif ghandle.B4_is_pressed():
        display.show(Image.ARROW_E)
        radio.send("255 100")
    else:
        display.clear()

