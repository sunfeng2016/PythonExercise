# -*- coding: utf-8 -*-
age = 20
if age >= 18:
    print("Your age is: %d" % age)
    print("adult")
print("\n*************************************\n")

age = 3
if age >= 18:
    print("Your age is", age)
    print("adult")
else:
    print("Your age is", age)
    print("teenager")
print("\n*************************************\n")

age = 3
if age >= 18:
    print("Your age is", age)
    print("adult")
elif age >= 6:
    print("Your age is", age)
    print("teenager")
else:
    print("Your age is", age)
    print("Kid")
print("\n*************************************\n")

s = input("birth: ")
birth = int(s)
if birth >= 2000:
    print("00后")
else:
    print("00前")
print("\n*************************************\n")

"""
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""
height = 1.75
weight = 80.5
BMI = weight / (height * height)
print("BMI: %.2f" % BMI)
if BMI < 18.5:
    print("过轻")
elif BMI < 25:
    print("正常")
elif BMI < 28:
    print("过重")
elif BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")