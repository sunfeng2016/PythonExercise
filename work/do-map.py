# -*- coding: utf-8 -*-
from collections import Iterable
"""
an example of map:
            f(x) = x * x
                  │
                  │
  ┌───┬───┬───┬───┼───┬───┬───┬───┐
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
[ 1   2   3   4   5   6   7   8   9 ]
  │   │   │   │   │   │   │   │   │
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
[ 1   4   9  16  25  36  49  64  81 ]
"""
def func(x):
    return x * x
L = list(range(1 , 10))
print(L)
R = map(func, L)
for r in R:
    print(r)
print("************************************")

print(list(map(func, L)))
print("************************************")

"""
利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']
"""

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
print("************************************")

def func(x):
  	return x * x
L = list(map(func, [1, 3, 5 , 7, 9]))
print(L)
print("************************************")

#an practice of map
def normalize(name):
  	name = name[0].upper() + name[1:].lower()
  	return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
print("************************************")