https://school.programmers.co.kr/learn/courses/30/lessons/258711
각 그래프의 특징을 파악하는 문제, 다른 이슈는 없음

```
"""
5:25 시작, 5:35 완료
"""
import sys
sys.setrecursionlimit(2**30)
from collections import defaultdict

def solution(edges):
    nodes = defaultdict(list)
    _node_incount = defaultdict(int)
    _node_outcount = defaultdict(int)
    for a, b in edges:
        nodes[a].append(b)
        # _nodes[b]
        _node_outcount[a] += 1
        _node_incount[a] += 0 # 활성화
        _node_incount[b] += 1
        
    root = 0
    # 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
    for i, count in _node_incount.items():
        if count == 0 and _node_outcount[i] >= 2:
            root = i
    
    
    def dfs(node, visited):
        if not nodes[node]:
            return 1 # 막대
        
        if _node_outcount[node] == 2:
            return 2 # 8자
        
        if node in visited:
            return 0
        
        visited.add(node)
        return dfs(nodes[node][0], visited)

            
    result = [0,0,0]
    for i in nodes[root]:
        node_type = dfs(i, set())
        result[node_type] += 1
    return [root] + result
```