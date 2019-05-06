# -*- coding: utf-8 -*-
import math
#define a function to calculate the absolute value
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print('abs(-1) = ', my_abs(-1))
print("******************************************")

#define a function to calculate the absolute value and exmine the error of argument
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x

print('abs(-1) = ', my_abs(-1))
print("******************************************")

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print("******************************************")

r = move(100, 100, 60, math.pi / 6)
print(r)
print("******************************************")

#define a function to calculate the two solutions of equation
def quardratic(a, b, c):
    T = b ** 2 - 4 * a * c
    if(T < 0):
        print("无解")
        return None
    else:
        x1 = (-b + math.sqrt(T)) / (2 * a)
        x2 = (-b - math.sqrt(T)) / (2 * a)
        print("有解")
        return x1, x2

#test the fuction
print('quadratic(2, 3, 1) = ', quardratic(2, 3, 1))
print('quadratic(1, 3, -4) = ', quardratic(1, 3, -4))
