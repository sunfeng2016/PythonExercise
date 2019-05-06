# -*- coding: utf-8 -*-

#key args

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Sarch', 20)
person('Michael', 21, city = 'BeiJing')
person('Bob', 43, gender = 'M', city = 'BeiJing', job = 'Engineer')
print("*******************************************")

extra = {'Job': 'engineer', 'Gender': 'M'}
person('Jack', 44, **extra)
print("*******************************************")

def person(name, age, *, city, job):
    print(name, age, city, job)
person('Sarach', 24, city = 'BeiJing', job = 'Engineer')
print("*******************************************")

#参数组合：必选参数、默认参数、可变参数、命令关键字参数、关键字参数
def f1(a, b, c = 0, *arg, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'arg:', arg, 'kw:', kw)

def f2(a, b, c = 0, *, d, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'kw:', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f2(1, 2, d = 99, ext = None)

print("*******************************************")
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
print("*******************************************")

def product(*args):
    mul = 1
    for x in args:
        mul = mul * x
    return mul
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))