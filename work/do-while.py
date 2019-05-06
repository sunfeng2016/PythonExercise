# -*- coding: utf-8 -*-
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("Sum = %d" % sum)
print("**********************\n")

L = ['Bart', 'Lisa', 'Adam']
for str in L:
    print(str)
print("**********************\n")

lenght = len(L)
i = 0
while i < lenght:
    print(L[i])
    i = i + 1  
print("**********************\n")

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
print("**********************\n")

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print("END")
print("**********************\n")