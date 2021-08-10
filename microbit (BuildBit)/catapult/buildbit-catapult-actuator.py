from microbit import *
import superbit

while True:
    a_state = button_a.is_pressed()
    b_state = button_b.is_pressed()
    if a_state and b_state:
        superbit.servo270(superbit.S1, 40)
        sleep(100)
        superbit.servo270(superbit.S1, 55)
        sleep(300)
        superbit.servo270(superbit.S1, 40)
    elif a_state:
        superbit.motor_control(superbit.M1, 64, 0)
        sleep(100)
        superbit.motor_control(superbit.M1, 0, 0)
    elif b_state:
        superbit.motor_control(superbit.M1, -64, 0)
        sleep(100)
        superbit.motor_control(superbit.M1, 0, 0)
