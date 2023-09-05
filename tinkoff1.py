# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:15:15 2023

@author: dimit
"""
stdin=input()
if len(stdin.split(' ')) < 2:
    raise Exception ("Please enter 2 numbers in first input!")
n, s = int(stdin.split(' ')[0]), int(stdin.split(' ')[1])
price_list = input()
lis1 = price_list.split(' ')
lis = [eval(j) for j in lis1]
maxi = 0
for i in range(int(n)):
    if (lis[i] <= s) and (lis[i] > maxi):
        maxi = lis[i]
print(maxi)
