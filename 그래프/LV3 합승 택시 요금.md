[틀림] 힌트를 보고 푼 문제이다. 함께 합승하는 지점을 돌아가면서 최적의 경로를 구하는게 필요하다

특히 플로이드 워셜 알고리즘을 적용할 때에는 '경유지' 루프가 가장 바깥쪽에 있어야한다는 사실을 기억하자.

이번 문제는 플로이드 워셜 알고리즘을 사용하는 경우, 가장 효율성이 좋았다.

[틀림] 1차 시도 방법
- (A, B)로 위치를 나타내고 
	- 둘이 같이 움직이는 경우, 한명만 움직이는 경우를 나타내고 다익스트라로 풀어보자.

```
from queue import PriorityQueue

def solution(n, s, a, b, fares):
    nodes = {}
    _temp = sorted([a, b])
    first_node = _temp[0]
    second_node = _temp[1]
    
    for i in range(1, n + 1):
        nodes[i] = {}
    for c, d, cost in fares:
        nodes[c][d] = cost
        nodes[d][c] = cost
            
    visited = set()
    queue = PriorityQueue()
    queue.put((0, (s, s)))
    
    def add(old_positions, new_positions, old_cost, add_cost):
        new_positions = tuple(sorted(new_positions)) # 최적화를 위해 항상 a<b
        
        # 이미 방문했으면 스킵
        if new_positions in visited:
            return None
        
        # 만약 a가 이미 목적지에 도달했는데 a의 위치가 변경되었다면 -> 스킵
        if old_positions[0] == first_node:
            if old_positions[0] != new_positions[0]:
                return None
    
        # 만약 b가 이미 목적지에 도달했는데 b의 위치가 변경되었다면 -> 스킵
        if old_positions[1] == second_node:
            if old_positions[1] != new_positions[1]:
                return None
        
        # 방문하지 않았으면
        new_cost = old_cost + add_cost
        queue.put((new_cost, new_positions))

        
    while not queue.empty():
        item = queue.get() 
        cost = item[0]
        positions = item[1]
        
        # 만약 a랑 b가 잘 도착해있고 이게 호출된거면 최적의 경로임.
        if positions[0] == first_node and positions[1] == second_node:
            return cost
        if positions in visited:
            continue
        visited.add(positions)
        # 같이 이동하는 시나리오
        if positions[0] == positions[1]: # 합승 상태에서만 움직일 수 있음
            for node in nodes[positions[0]]:
                result = add(positions, (node, node), cost, nodes[positions[0]][node])
        
        # a만 움직이는 시나리오
        for node in nodes[positions[0]]:
            result = add(positions, (node, positions[1]), cost, nodes[positions[0]][node])

        # b만 움직이는 시나리오
        for node in nodes[positions[1]]:
            result = add(positions, (positions[0], node), cost, nodes[positions[1]][node])
```


[일부 틀렸지만 수정 후 완료] 다익스트라 풀이
- for n in nodes:
	- start -> n 비용 + n -> a 비용 + n -> b 비용으로 풀기
	- 다익스트라를 활용하는 방법
	- 최적화 포인트에 대한 고민을 잘 해보자.
		- 1. 우선순위 큐에서 get() 되는 경우가 최소 지점이다. 넣는 순간은 최소가 아닐 수 있다.
		- 2. 최적화 포인트 1 -> 이미 방문한곳으로 가는 경로는 queue에 넣지 않는다.
		- 3. 최적화 포인트 2 -> 이미 방문한 노드인 경우 추가 노드 탐색조차 생략한다.

```
from queue import PriorityQueue

def solution(n, s, a, b, fares):
    nodes = {
        i: {} for i in range(1, n + 1)
    }
    
    for c, d, cost in fares:
        nodes[c][d] = cost
        nodes[d][c] = cost
    
    def function(start_node, end_node):
        
        visited = set()
        queue = PriorityQueue()
        queue.put((0, start_node))
        while not queue.empty():
            cost, current_node = queue.get()
            if current_node in visited:
                continue
            # 여기에 뜨면 이게 해당 위치로 가기 위한 최소
            
            visited.add(current_node)
            if current_node == end_node:
                return cost
            
            for next_node in nodes[current_node]:
                if next_node not in visited:
                    add_cost = nodes[current_node][next_node]
                    queue.put((cost+add_cost, next_node))
        return -1
    # 중간 n을 거쳐서 가는 방법
    min_cost = 1e9 * 1e9
    for n in range(1, n + 1):
        cost = function(s, n)
        if cost == -1:
            continue
        
        cost += function(n, a)
        cost += function(n, b)
        min_cost = min(cost, min_cost)
    return min_cost
        
        
```



[틀림] 플로이드워셜 알고리즘
- 중요 1: 같은 노드를 방문 하는 경우에는 비용 0
- 중요 2: 양방향 그래프인 경우 양쪽으로 cost 등록을 해줘야한다.
- 중요 3: 경유지 반복문이 가장 바깥쪽에 있어야한다.


```
from queue import PriorityQueue

def solution(n, s, a, b, fares):
    # 플로이드 워셜 알고리즘
    
    # 0번줄, 0번 행은 무시
    distances = [[1e9] * (n+1) for i in range(n+1)]
    
    # 중요 1: 같은 노드를 방문 하는 경우에는 비용 0
    for x1 in range(1, n+1):
        distances[x1][x1] = 0
    
    # 중요 2: 양방향 그래프인 경우 양쪽으로 cost 등록을 해줘야한다.
    for c, d, cost in fares:
        distances[c][d] = cost
        distances[d][c] = cost
    
    # 중요 3: 경유지 반복문이 가장 바깥쪽에 있어야한다.
    for x2 in range(1, n+1):
        for x1 in range(1, n+1):
            for x3 in range(1, n+1):
                new_cost = distances[x1][x2] + distances[x2][x3]
                distances[x1][x3] = min(distances[x1][x3], new_cost)
    
    min_cost = 1e9
    for x1 in range(1, n+1):
        new_cost = distances[s][x1] + distances[x1][a] + distances[x1][b]
        min_cost = min(new_cost, min_cost)
    return min_cost
```