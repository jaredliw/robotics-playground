from microbit import *
import radio
import math
import ghandle

def bound(val, min_val, max_val):
    if val < min_val:
        return min_val
    elif val > max_val:
        return max_val
    else:
        return val

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def get_magnitude(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_rotation_angle(ori_x, ori_y, p1_x, p1_y, p2_x, p2_y):
    length_p1_p2 = get_magnitude(p1_x, p1_y, p2_x, p2_y)
    length_ori_p1 = get_magnitude(ori_x, ori_y, p1_x, p1_y)
    length_ori_p2 = get_magnitude(ori_x, ori_y, p2_x, p2_y)
    try:
        return 180 - math.degrees(math.acos((length_ori_p2 ** 2 + length_ori_p1 ** 2 - length_p1_p2 ** 2) / (2 * length_ori_p2 * length_ori_p1)))
    except ZeroDivisionError:
        return 0

ORI_X, ORI_Y = ghandle.get_value_x(), ghandle.get_value_y()
RADIUS = 508
radio.on()
while True:
    x = bound(ghandle.get_value_x(), ORI_X - RADIUS, ORI_X + RADIUS)
    y = bound(ghandle.get_value_y(), ORI_Y - RADIUS, ORI_Y + RADIUS)
    speed = int(map_range(get_magnitude(x, y, ORI_X, ORI_Y), 0, RADIUS, 0, 255))
    angle = int(get_rotation_angle(ORI_X, ORI_Y, ORI_X, ORI_Y + RADIUS, x, y))
    if angle > 90:
        angle = 180 - angle
        backwards = True
    else:
        backwards = False
    motor_diff = int(map_range(angle, 0, 90, 0, speed))
    if x > ORI_X:
        left, right = speed - motor_diff, speed
    else:
        left, right = speed, speed - motor_diff
    if backwards:
        left *= -1
        right *= -1
    radio.send("{} {}".format(left, right))
