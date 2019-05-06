# -*- coding: utf-8 -*-
from functools import reduce
"""
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
#sum
def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3, 4, 5]))
print("*****************************************")

#connect

def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 2, 3, 4, 5]))
print("*****************************************")

def chartonum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(chartonum, '13579')))
print("*****************************************")

#strtoint

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def strtoint(s):
    def fn(x, y):
        return x * 10 + y
    def chartonum(s):
        return DIGITS[s]
    return reduce(fn, map(chartonum, s))

print(strtoint('1234567'))
print("*****************************************")

#lambda

def chartonum(s):
    return DIGITS[s]

def strtoint(s):
    return reduce(lambda x, y: x * 10 + y, map(chartonum, s))
print(strtoint('1234567'))
print("*****************************************")

"""
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用
reduce()求积
"""
def prod(L):
    def Mul(x, y):
        return x * y
    return reduce(Mul, L)
print(prod([1, 2, 3, 4, 5 , 6]))
print("*****************************************")

#测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
print("*****************************************")

"""
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456：
"""

def strtoint(s):
    def chartonum(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    def fninteger(x, y):
        return x * 10 + y
    def fndecimal(x, y):
        return x / 10 + y
    dotIndex = s.index('.')
    return reduce(fninteger, map(chartonum, s[ : dotIndex])) + reduce(fndecimal, list(map(chartonum, s[dotIndex + 1 : ]))[ : : -1]) / 10
print(strtoint('123.4567'))

print("*****************************************")
def add(x, y):
    return x * y

print(reduce(add, [1, 2, 3, 4, 5]))
print("*****************************************")

def listtoint(L):
    def func(x, y):
        return x * 10 + y
    return (reduce(func, L))

print(listtoint([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print("*****************************************")

def str2int(s):
    def func(x, y):
        return x * 10 + y
    def char2num(s):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[s]
    return reduce(func, list(map(char2num, s)))
print(str2int('123456'))
print("*****************************************")
