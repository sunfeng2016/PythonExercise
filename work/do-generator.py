# -*- coding: utf-8 -*-
"""
高级特性：生成器generator
"""

s = (x * x for x in range(10))
print(s)
for n in s:
    print(n)
print("***********************************")

#Fibonacci数列:1, 1, 2, 3, 5, 8, 13, 21, 34....
#approach1
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
print("***********************************")

#approach2: generactor
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b         #Generator
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(10)
print('fib(10): ', f)
for x in f:
    print(x)
print("***********************************")

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#test
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
print(next(o))
print("***********************************")
print(next(o))
print("***********************************")
print(next(o))
print("***********************************")

"""
练习
杨辉三角定义如下：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
"""
def triangles():
    L = [1]
    while True:
        yield L[: len(L)]
        #yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
t = triangles()
for x in range(10):
    print(next(t))
print("***********************************")
#test
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
print("***********************************")