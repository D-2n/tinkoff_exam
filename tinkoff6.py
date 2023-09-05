# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:53:03 2023

@author: dimit
"""

#dict for tracking number of gangs
stdin = input()
n, m = int(stdin.split(' ')[0]), int(stdin.split(' ')[1])
track = {}
for i in range(1,n+1):
    track[i] = 1 # initial solo gangs
glist = []
for i in range(1,n+1):
    glist.append([i])
for _ in range(m):
    r1 = [eval(j) for j in input().split(' ')]
    #gang merge
    code = r1[0]
    if code == 1:
        x = r1[1]
        y = r1[2]
        i1 = -1
        i2 = -1
        for j in range(len(glist)):
            if x in glist[j]:
                i1 = j
            if y in glist[j]:
                i2 = j
        if i1 == i2:
            break
        if (i1 != -1) and (i2 != -1):
            new=glist[i1]+glist[i2] #new list
            #update gangnumber
            #delete old lists
            #add new one
            for i in new:
                track[i]+=1
            remove1=glist[i1]
            remove2=glist[i2]
            glist.remove(remove1)
            glist.remove(remove2)
            glist.append(new)
    if code == 2:
        x = r1[1]
        y = r1[2]
        i1 = 0
        i2 = 0
        for j in range(len(glist)):
            if x in glist[j]:
                i1 = j
            if y in glist[j]:
                i2 = j
        if i1 == i2:
            print('YES')
        else:
            print('NO')
    if code == 3:
        print(track[r1[1]])
