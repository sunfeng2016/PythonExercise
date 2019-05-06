# -*- coding: utf-8 -*-
"""
高级特性：切片
"""
#creat a list of 0-99
L = list(range(100))
print(L)
print("************************************")

#access 0-10
print(L[ : 10])
print("************************************")

#access 90-99
print(L[90 : ])
print("************************************")

#access 11-20
print(L[11 : 21])
print("************************************")

#access 0-10 and can be divisible by 2
print(L[0 : 10 : 2])
print("************************************")

#access all and can be divisible by 5
print(L[ : : 5])
print("************************************")

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格

def trim(str):
    first = 0
    last =  1
    while first < len(str):
        if str[first] != ' ':
            break
        first = first + 1
    while last <= len(str):
        if str[-last] != ' ':
            break
        last = last + 1
    return str[first : (len(str) - last + 1)]
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
print("************************************")