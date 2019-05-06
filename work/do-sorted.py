# -*- coding: utf-8 -*-

print(sorted([36, 5, -12, 9, -21]))
print("***********************************")

print(sorted([36, 5, -12, 9, -21], key = abs))
print("***********************************")

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))
print("***********************************")

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))
print("***********************************")

"""
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
"""

def by_name(t):
    return t[0].lower()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key = by_name))
print("***********************************")

#再按成绩从高到低排序：

def by_score(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key = by_score, reverse = True))
print("***********************************")