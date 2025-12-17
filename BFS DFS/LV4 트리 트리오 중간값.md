---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/68937
문제 유형:
  - DFS
풀이 날짜: 2025-12-17
정답 여부: 정답
틀린 이유:
마지막 풀이 날짜:
---
트리가 주어졌을 때 세 점을 선택해서 세 점 각각의 거리 값의 중간 값이 최대가 되도록 하는 문제.

n은 20만이므로 모든 경우의 수를 찾으려고 하면 시간 초과가 발생한다.
- nlogn을 사용하거나 n 으로 완료할 수 있는 방법을 찾아야한다.

이 문제의 정답인 3개의 점을 선택하기 위한 케이스를 생각해보면 서로 가장 멀리있는 두 점을 선택해야한다.
- 그리고 트리에서 어떤 한 점을 기준으로 가장 먼 거리의 점을 선택하게 되면, 두 점중 하나가 될 것이라는 것을 예상할 수 있다.

이 방법으로 점을 하나씩 찾아간다.

마지막으로 중간 점을 선택해야하는데 for(n)을 사용하여 거리를 재확인한다.
거리 정보는 list 자료형을 사용하여 미리 계산해두고 사용한다.


```
"""
두 점의 거리: 간선의 개수

변수
- n 3~25만
- 트리구조

제일 큰 값을 가져가려면
모든 leaf 노드 확인
- 가장 트리가 깊은 지점 선택
- 나머지 각각 구하면서 제일 먼저 선택

"""
from itertools import combinations
from collections import defaultdict
import sys
sys.setrecursionlimit(2**30)

def solution(n, edges):
    leaf_nodes = set()
    nodes = defaultdict(set)
    answer = 0
    
    for a, b in edges:
        nodes[a].add(b)
        nodes[b].add(a)
    for i in nodes:
        if len(nodes[i]) == 1:
            leaf_nodes.add(i)
    # 가장 거리가 먼 두점 찾기
    def dfs(temps, node, count):
        if node in temps:
            return
        temps[node] = count
        for child in nodes[node]:
            dfs(temps, child, count + 1)
    def select(temps):
        max_count = max(temps.values())
        for i, j in temps.items():
            if j == max_count:
                return i
            
    temps = {}
    dfs(temps, 1, 0)
    first_point = select(temps)
    
    first_distances = {}
    second_distances = {}
    
    dfs(first_distances, first_point, 0)
    second_point = select(first_distances)
    dfs(second_distances, second_point, 0)
    def function(a, b):
        if a == first_point:
            return first_distances[b]
        if a == second_point:
            return second_distances[b]

    answer = 0
    for i in range(1, n+1):
        result = []
        if i == first_point:
            continue
        if i == second_point:
            continue
        result.append(function(first_point, second_point))
        result.append(function(first_point, i))
        result.append(function(second_point, i))
        result.sort()
        answer = max(answer, result[1])
    return answer
```