# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:40:32 2023

@author: dimit
"""
# changed the iteration to avoid calling count() inside the loop, reducing the overall
# complexity from O(n^2) to O(n)
stringy = input()
lets = {'s' : 0, 'h' : 0, 'e' : 0, 'r' : 0, 'i' : 0, 'f' : 0}
for i in stringy:
    if i in lets:
        lets[i] +=1
lets['f'] = lets['f']//2
print(min(lets.values()))