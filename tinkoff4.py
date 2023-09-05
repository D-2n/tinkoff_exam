# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 13:25:07 2023

@author: dimit
"""

stdin = input()
n, m = int(stdin.split(' ')[0]), int(stdin.split(' ')[1])
lis1 = input().split(' ')
lis = lis1 + lis1
k = 0
kup_list = []
lis = sorted([eval(j) for j in lis])

def joe(lis, m, target):
    if (target == 0):
        return True
    if (m == 0):
        return False
    if (lis[m - 1] > target):
        return joe(lis, m - 1, target)
    elif joe(lis, m-1, target):
        return True
    elif joe(lis, m-1, target-lis[m-1]):
        global kup_list
        kup_list.append(lis[m-1])
        global k
        k+=1
        return True
res = joe(lis, 2*m,n)
if res == None:
    print(-1)
else:
    print(k)
    for i in kup_list:
        print(i)