# -*- coding: utf-8 -*-

#location args

def power(x):
    return x ** 2

print("10 ** 2 =", power(10))
print("***************************")

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print("2 ** 10 =", power(2, 10))
print("***************************")

#default args

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print("10 ** 2 =", power(10))
print("2 ** 10 =", power(2, 10))
print("***************************")

def enroll(name, gender, age = 6, city = 'BeiJing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')
print("***************************")
enroll('Bob', 'M', 7)
print("***************************")
enroll('Tom', 'M', 8, 'Tianjin')
print("***************************")

#a trap of default args
def add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())
print("***************************")

#the solution of the trap
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())
print("***************************")

#variable args
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#calc 1到10的平方和
sum1 = calc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sum1)
sum2 = calc((1, 2, 3))
print(sum2)
print("***************************")

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
sum1 = calc(1, 2, 3)
print(sum1)
sum2 = calc(1, 6, 7)
print(sum2)
num = [1, 6, 7]
sum3 = calc(num[0], num[1], num[2])
print(sum3)
sum4 = calc(*num)
print(sum4)
print("***************************")