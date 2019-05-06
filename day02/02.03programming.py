"""
Day2 表达式及控制语句
03 程序的基本编写方法(IPO)
"""
# 输入数据
# 处理数据
# 输出数据

print("##################################")
##################################
#实例1 圆面积的计算
#输入：圆半径radius
#处理：计算圆的面积 area = pei * radius * radius
#输出：圆面积area

radius = 25
area = 3.1415 * radius * radius
print(area)
print("面积: %-10.2f" %area)
print("面积: {:.2f}".format(area))
print("##################################")

##################################
#实例2 格式化输出浮点数

pi = 3.141592653
print("%10.3f" % pi)            #字段宽度为10，精度为3
print("pi = %.*f" % (3, pi))    #用*从后面的元组中读取字段宽度或精度
pi = 3.142
print("%010.3f" % pi)           #用0填充空白
print("%-10.3f" % pi)           #左对齐
print("%+f" % pi)               #显示正负
print("##################################")

##################################
#实例3 Print自动换行和不换行
for i in range(0,6):            #print会自动在行末加上回车
    print(i)                    #若不需要回车，只需在print
for i in range(0,6):            #尾部添加一个逗号，即可改变
    print(i,end = "")           #它的行为
print("")
print("##################################")

##################################
#实例4 print.format用法
print('{0},{1}'.format('zhangk',32))
print('{},{},{}'.format('zhangk','boy',32))
print('{name},{sex},{age}'.format(age = 32,sex = 'male',name = 'zhangk'))

#格式限定符
#它有着丰富的“格式限定符”，语法是{}中带:号
#填充与对齐
#填充长跟对齐一起使用
#'、<、>分别是居中、左对齐、右对齐，后面带宽度
#:好跟带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{: >8}'.format('zhang'))
print('{:0>8}'.format('zhang'))
print('{:a<8}'.format('zhang'))
print('{:p^9}'.format('zhang'))

#精度与类型f
print('{:.2f}'.format(31.31613))

#进制
#b 二进制
#d 十进制
#o 八进制
#x 十六进制

print('{:b}'.format(15))
print('{:o}'.format(15))
print('{:d}'.format(15))
print('{:x}'.format(15))

#用逗号做金额的千位分隔符
print('{:,}'.format(123456789))
print("##################################")

##################################
#实例4 简单的人名对话
#name = input("输入姓名: ")
name = "孙峰"
print('{}同学，学好Python，前途无量!'.format(name))
print('{}大侠，学好Python, 前途无量!'.format(name[0]))
print('{}哥哥，学好Python，前途无量!'.format(name[1:]))
print("##################################")

##################################
#实例5 斐波那契数列的计算
a, b = 0, 1
while a < 1000:
    print(a, end = ",")
    a, b = b, a+b
print("")
print("##################################")

##################################
#实例6 日期和时间的输出
#输出当前的日期和时间
from datetime import datetime
now = datetime.now()
print("当前日期和时间: ",now)
print("当前日期：",now.strftime("%x"))
print("当前时间：",now.strftime("%X"))
print("##################################")

##################################
#实例7 字符串拼接
str1 = input("请输入一个人的名字:");
str2 = input("请输入一个国家的名字:");
print("世界这么大，{}想去{}看看".format(str1,str2))
print("##################################")

##################################
#实例8 求前N项和
str1 = input("请输入一个整数:");
n = int(str1)
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("前{}项和为: {}".format(n,sum))