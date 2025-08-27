

그래프 - 다익스트라 OR BFS
- 점들을 nodes[node_id] = [] 이렇게 연결하자.
- 그리고 양방향으로 이동할 수 있으면 다 넣자.
- BFS 혹은 우선순위 큐를 사용하고, 앞에서부터 꺼내서 distances 업데이트, 반복하면 된다.
	- BFS를 사용할 수 있는 건 거리가 항상 1일때이다.

```from collections import deque

def print(*args, **kwargs):
    ...
def solution(n, edge):
    nodes = {}
    
    for _n1, _n2 in edge:
        n1 = _n1 - 1
        n2 = _n2 - 1
        if n1 not in nodes:
            nodes[n1] = []
        if n2 not in nodes:
            nodes[n2] = []
            
        nodes[n1].append(n2)
        nodes[n2].append(n1)
        
    distances = [None] * n
    distances[0] = 0
    
    queue = deque([0])
    while queue:
        node = queue.popleft()
        print("이동 기준점", node)
        for n2 in nodes[node]:
            new_distance = distances[node] + 1 # 현재에서 이동하는 경우
            if distances[n2] is None or distances[n2] > new_distance:
                
                distances[n2] = new_distance
                queue.append(n2)
                print(distances)
            
                
    print(distances)
    answer = 0
    max_distance = None
    for d in distances:
        if d is None:
            continue
        if max_distance is None or max_distance < d:
            max_distance = d
    
    for i in distances:
        if i == max_distance:
            answer += 1
    return answer
```