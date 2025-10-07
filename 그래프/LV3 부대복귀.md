https://school.programmers.co.kr/learn/courses/30/lessons/132266

수 많은 출발지에서 목적지로 가는 최단 경로를 구하는 문제다.

무방향 그래프이므로 목적지에서 출발한다는 아이디어로 바꾸면 다익스트라 알고리즘으로 해결이 가능하다.
- 특정 지점에서 모든 지점으로 향하는 최단 경로 테이블을 만들 수 있기 때문

```
"""
두 지역 길을 통과하는데 걸리는 시간 1

최단 시간(경로)로 부대 복귀 예정이나, 적군의 방해(장애물)로 복귀가 불가능한 부대원이 있을 수 있음.

--- 문제 해석
총 500명이 이동하는 시나리오다. 500명의 시작 위치는 모두 다르다.
길 왕복 - 무방향 그래프
n개의 지역이 있다.
목적지는 모두 동일하다.

플로이드 워셜 알고리즘 사용 불가 - n이 너무 큼.
다익스트라 -> 시작 지점은 모두 다르지만, 목적지에서 출발하는 개념으로 볼 수 있다.
"""
from collections import deque
def solution(n, roads, sources, destination):
    nodes = {}
    for i in range(1, n+1):
        nodes[i] = []
    
    for a, b in roads:
        nodes[a].append(b)
        nodes[b].append(a)
    
    MAX_DISTANCE = 10**100
    distances = [MAX_DISTANCE] * (n+1)
    queue = deque()
    queue.append([destination, 0])
    visited = [False] * (n+1)
    while queue:
        current_node, d = queue.popleft()
        if visited[current_node]:
            continue
        visited[current_node] = True
        distances[current_node] = d
        for next_node in nodes[current_node]:
            if visited[next_node]: # 가지치기
                continue
            queue.append([next_node, d+1])
    
    answer = []
    for i in sources:
        d = distances[i]
        if d == MAX_DISTANCE:
            answer.append(-1)
        else:
            answer.append(d)
    return answer
```