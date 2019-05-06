# -*- coding: utf-8 -*-

from collections import Iterable
import math

"""
高级特性:迭代
"""
#判断对象是否可迭代
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))
print("******************************************")

#取下标：enumerate
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print("******************************************")

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))
print("******************************************")

#iter list
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print("******************************************")

d = {'a': 1, 'b': 2, 'c': 3}
#iter each key:
print('Iter Key:', d)
for k in d.keys():
    print('key:', k)

#iter each value
print('Iter value:', d)
for v in d.values():
    print('value:', v)

#iter both key and value
print('Iter item:', d)
for k, v in d.items():
    print('item:', k, v)
print("******************************************")

#iter list with index
L = ['A', 'B', 'C', 'D']
print('iter enumrate(', L, ')')
for i, value in enumerate(L):
    print(i, value)

#iter list with index
L = [(1, 1), (2, 4), (3, 9)]
print('iter', L)
for x, y in L:
    print(x, y)
print("******************************************")

#请使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(L):
    if L == []:
        return (None, None)
    Max = 0
    Min = L[0]
    for x in L:
        Max = max(Max, x)
        Min = min(Min, x)
    return (Min, Max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
print("******************************************")