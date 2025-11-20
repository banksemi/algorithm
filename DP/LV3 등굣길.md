---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/42898
문제 유형:
  - DP(Bottom-up)
  - DP(Top-down)
  - BFS
풀이 날짜: 2025-11-20
정답 여부: 오답
틀린 이유:
  - 좌표 오류
마지막 풀이 날짜:
---
특정 경로로 가는 모든 경로의 수를 세는 문제, DP(topdown, bottomup)과 최단 경로 알고리즘 모두 사용이 가능하다.

DP(Bottom-up)
```
"""

DP or 다익스트라?
m = x 좌표 
n = y 좌표


"""

def solution(m, n, puddles):
    width = m
    height = n
    puddle = set()
    for x, y in puddles:
        puddle.add((x-1,y-1))
        
    board = [[0] * width for _ in range(height)]
    
    board[0][0] = 1
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue
            if (x, y) in puddle:
                continue
            board[y][x] = board[y][x-1]
            if y > 0:
                board[y][x] += board[y-1][x]
            board[y][x] %= 1_000_000_007  
            
    return board[height-1][width-1]
```


DP(top-down)
```
import sys

from functools import lru_cache

sys.setrecursionlimit(2**30)
def solution(m, n, puddles):
    puddles_set = set()
    for x, y in puddles:
        puddles_set.add((x-1,y-1))
        
    @lru_cache(maxsize=None)
    def dfs(x, y):
        if x == 0 and y == 0:
            return 1
        
        if (x,y) in puddles_set:
            return 0
        
        count = 0
        if x > 0:
            count += dfs(x-1, y)
        if y > 0:
            count += dfs(x, y-1)
        return count % 1_000_000_007
    return dfs(m-1, n-1)
```

BFS (거리가 1인 다익스트라)
```
from collections import deque
dirs = [(1,0), (0, 1)]


def solution(m, n, puddles):
    def get_tiles(x, y):
        for ix, iy in dirs:
            if x + ix == m:
                continue
            if y + iy == n:
                continue
            yield x + ix, y + iy
        
    answer = 0
    puddles_set = set()
    for x, y in puddles:
        puddles_set.add((x-1, y-1))
    
    queue = deque([(0, 0)])
    board = [[0] * n for _ in range(m)] # board[x][y]
    board[0][0] = 1
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x,y) in visited:
            continue
        
        visited.add((x,y))
        for new_x, new_y in get_tiles(x, y):
            if (new_x, new_y) in puddles_set:
                continue
                
            # 방문 여부와 상관 없이 가능한 카운트를 더한다.
            board[new_x][new_y] += board[x][y]
            board[new_x][new_y] = board[new_x][new_y] % 1_000_000_007
            
            if (new_x, new_y) in visited:
                continue
            queue.append((new_x,new_y))
    
    return board[m-1][n-1]
```