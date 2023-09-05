# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:58:22 2023

@author: dimit
"""

n = int(input())
joe = input().split(' ')
win = input().split(' ')
m1 = 0
m2 = 0
for i in range(n):
    if joe[i] != win[i]:
        m1 = i
        break
for i in reversed(range(n)):
    if joe[i] != win[i]:
        m2 = i + 1
        break
sortpart = joe[:m1 ] + sorted(joe[m1:m2]) + joe[m2:]
if sortpart == win:
    print ('YES')
else:
    print('NO')
