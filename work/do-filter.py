# -*- coding: utf-8 -*-

#filter 过滤

"""
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用
于每个元素，然后根据返回值是True还是False决定
保留还是丢弃该元素。
"""
#删除一个列表中的偶数
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15]))
print(L)
print("****************************************")

#删除一个序列中的空字符串
def not_empty(s):
    return s and s.strip()
L = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(L)
print("****************************************")

#用filter求素数

#step1: 用生成器构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#step2: 定义一个筛选函数
def _not_divisable(n):
    return lambda x: x % n > 0

#step3: 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()    #初始序列
    while True:
        n = next(it)    #返回序列
        yield n
        it = filter(_not_divisable(n), it) #构造新序列

#打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
print("****************************************")