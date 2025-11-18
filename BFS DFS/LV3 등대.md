---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/133500
문제 유형:
  - BFS
  - DFS
  - 그래프
풀이 날짜: 2025-11-18
정답 여부: 오답
틀린 이유:
  - 논리 오류
마지막 풀이 날짜:
---
BFS 방식으로 문제를 풀다가 해결이 안되서 DFS 방식으로 다시 문제를 풀었던 문제
```
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(2**30)
def solution(n, lighthouse):
    answer = 0
    leafs = deque()
    nodes = defaultdict(set)
    for a, b in lighthouse:
        nodes[a].add(b)
        nodes[b].add(a)
    leafs = set()
    for i in range(1, n+1):
        if len(nodes[i]) == 1:
            leafs.add(i)
            
    visited = set()
    def dfs(node):
        nonlocal answer
        visited.add(node)
        if node in leafs and node != 1:
            return True # 불빛이 필요함
        
        need_light = False
        for i in nodes[node]:
            if i in visited:
                continue
            if dfs(i):
                need_light = True
        
        # 하위 노드에서 불이 필요하다고 한다면
        if need_light:
            answer += 1
            return False
        
        else: # 하위 노드는 자체적으로 처리되었고 이 노드에 대한 상위 등대와의 불빛이 필요함
            return True 
    
    dfs(1)
    return answer
```