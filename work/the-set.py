# -*- coding: utf-8 -*-
s = set([1, 2, 3])
print(s)
print("************************")
s = set([1, 2, 2, 2, 3, 3])
print(s)
print("************************")
s.add(4)
print(s)
print("************************")
s.remove(4)
print(s)
print("************************")

set1 = set([1, 2, 3])
set2 = set([2, 3, 4])
print(set1 & set2)
print(set1 | set2)
print("************************")

#不可变对象与可变对象
#可变对象: list
a = ['c', 'a', 'b']
a.sort()
print(a)
print("************************")
#不可变对象: tuple, key, str, int, float等
a = 'abc'
b = a.replace('a', 'A')
print(a) 
print(b)
print("************************")