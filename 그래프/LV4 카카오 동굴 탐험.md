---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/67260
문제 유형:
  - 그래프
  - 트리
  - BFS
풀이 날짜: 2025-12-26
정답 여부: 오답
틀린 이유:
  - 예외처리
마지막 풀이 날짜:
---

트리를 탐색하며, 일부 요소의 선행 방문 조건이 있을 때 대응하는 문제.
트리는 0번부터 시작한다는 전제 조건이 있으며, 0번 노드를 방문할 수 없는 경우가 있기 때문에 예외 처리가 필요했다.

```
"""
2:42
3:02 (정확성 1문제 틀림, 약 98점) -> 3:04 해결
조건
- 시작 지점(유일한 입구) 0번
- 양방향 통행 가능, 두 방을 직접 연결하는 길은 하나
- 서로 다른 두 방 사이의 최단 경로는 한개 (n-1개의 경로가 있으므로 트리 구조)
- 이동 불가 케이스는 없음

탐험 계획
- 모든 방 한번은 방문
- 특정 방을 방문하기 전 먼저 방문해야할 방이 있다.(or 없다)
- 먼저 방문해야하는 방의 번호는 유니크하다.
- a->b이면서 b->a는 없다.

풀이 계획
- 일단 방문이 가능한 경로는 계속 탐색 큐에 넣는다.
- 조건을 만족하지 않으면 임시 큐에 넣는다.

queue
visited
"""
from collections import defaultdict, deque

def solution(n, path, order):
    nodes = defaultdict(set)
    orders = defaultdict(set)
    for a, b in path:
        nodes[a].add(b)
        nodes[b].add(a)
        
    degrees = defaultdict(int)
    for a, b in order:
        orders[a].add(b)
        degrees[b] += 1
    
    if degrees[0] != 0:
        return False
    queue = deque([0])
    visited = set()
    waited = set()
    while queue:
        node = queue.popleft()
        
        # 한번만 방문 처리
        if node in visited:
            continue
        visited.add(node)
        
        # 순서가 있는 경우 순서 차수를 제거.
        for child in orders[node]:
            degrees[child] -= 1
            # 이미 방문 가능했던 상태지만 차수가 있어서 기다렸던 경우, 이제 queue에 추가
            if child in waited and degrees[child] == 0:
                queue.append(child)
                waited.remove(child)
        
        # 하위 노드를 방문 후보에 등록
        for child in nodes[node]:
            # 차수가 없으면 바로 등록
            if degrees[child] == 0:
                queue.append(child)
            else: # 차수가 남아있으면 다른 노드의 orders 처리에서 함께 처리되도록 등록
                waited.add(child)
    return len(visited) == n
```