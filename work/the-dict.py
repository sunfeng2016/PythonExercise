# -*- coding: utf-8 -*-
d = {'SunFeng': 100, 'XuFeng': 97, 'WangFeng': 99}
print(d['SunFeng'])
print("**************************\n")
d['WoXiang'] = 90
for names in d:
    print(names, ":", d[names])
print("**************************\n")
d.pop('XuFeng')
for names in d:
    print(names, ":", d[names])
print("**************************\n")