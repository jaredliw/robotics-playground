from microbit import *
import radio
import superbit

radio.on()
while True:
    command = radio.receive()
    if command is not None:
        left, right = map(int, command.split())
        superbit.motor_control_dual(superbit.M1, superbit.M3, left, right, 0)
    else:
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)
