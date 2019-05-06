# -*- coding: utf-8 -*-
import os #导入os模块
"""
列表生成式
List Comprehensions
"""
#create a list:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list(range(1, 11))
print(L)
print("*******************************")

#create a list:[1x1, 2x2, 3x3, ..., 10x10]
#approach 1
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
print("*******************************")

#approach 2
L = [x * x for x in range(1, 11)]
print(L)
print("*******************************")

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
print("*******************************")

L = [m + n for m in 'ABC' for n in 'XYZ']
print(len(L))
print(L)
print("*******************************")

direction = [d for d in os.listdir('.')]    #os.listdir()可以列出文件和目录
print(direction)
print("*******************************")

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = [k + '=' + v for k, v in d.items()]
print(L)
print("*******************************")

L1 = ['Hello', 'World', 'IBM', 'Apple']
L2 = [s.lower() for s in L1]
print(L2)
print("*******************************")

#practice 
L1 = ['Hello', 'World', 18, 'IBM', 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
print("*******************************")

