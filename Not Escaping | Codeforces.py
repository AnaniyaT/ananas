# https://codeforces.com/contest/1627/problem/E

from collections import defaultdict
from sys import stdin

input = stdin.readline

tests = int(input())
inf = -float('inf')

for _ in range(tests):
    n, m, k = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    
    ladders = [[] for _ in range(n)]
    for _ in range(k):
        a, b, c, d, h = list(map(int, input().split()))
        ladders[a - 1].append((b - 1, c - 1, d - 1, h))
    
    floors = [{} for _ in range(n)]
    for florInd, floor in enumerate(ladders):
        for b, c, d, h in floor:
            floors[florInd][b] = inf
            floors[c][d] = inf
    
    floors[0][0] = 0
    floors[n-1][m-1] = inf
    
    for floorInd in range(n):
        floor = floors[floorInd]
        cols = sorted(floor.keys())
        # print(cols)
        
        for ind in range(1, len(cols)):
            floor[cols[ind]] = max(floor[cols[ind]], floor[cols[ind-1]] - (xs[floorInd] * abs(cols[ind] - cols[ind-1])))
        for ind in range(len(cols)-2, -1, -1):
            floor[cols[ind]] = max(floor[cols[ind]], floor[cols[ind+1]] - (xs[floorInd] * abs(cols[ind] - cols[ind+1])))
        for b, c, d, h in ladders[floorInd]:
            floors[c][d] = max(floors[c][d], floors[floorInd][b] + h)
        
 
    ans = -floors[n-1][m-1]
    
    print(ans if ans != -inf else "NO ESCAPE")
