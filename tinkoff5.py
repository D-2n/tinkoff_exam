# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:05:20 2023

@author: dimit
"""
import copy
stdin = input()
n, m = int(stdin.split(' ')[0]), int(stdin.split(' ')[1])
lis = [[[] for _ in range(n)] for _ in range(n)]
maxroad = 0
for i in range (m):
    r1 = [eval(j) for j in input().split(' ')]
    lis[r1[0]-1][r1[1]-1].append(r1[2])
    lis[r1[1]-1][r1[0]-1].append(r1[2])
    if r1[2] > maxroad:
        maxroad = r1[2]
def count_state(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in range(len(graph)):
            if graph[node][neighbor] != [] and neighbor not in visited:
                dfs(neighbor)

    visited = set()
    components = 0

    for node in range(len(graph)):
        if node not in visited:
            dfs(node)
            components += 1

    return components

statecount = count_state(lis)
result = 0
max_destroyed = 0
for i in range(maxroad):
    destroyed = 0
    lis1=copy.deepcopy(lis)
    for j in range(n):
        for k in range(n):
            if lis1[j][k]!=[]:
                for road in range(len(lis1[j][k])):
                    if lis[j][k][road] <= i:
                        lis1[j][k].remove(lis[j][k][road])
                        destroyed +=1
    if statecount == count_state(lis1) and destroyed >= max_destroyed:
        max_destroyed = destroyed
        result = i
print(result)
        