https://school.programmers.co.kr/learn/courses/30/lessons/62050

격자형 보드 안에서 최소한의 사다리를 넣어 모든 지역을 이동 가능하게 만드는 문제이다.

풀이 방법
- 격자형 보드에서 움직일 수 있는 경우(최대 4 방향)을 edge로 비용과 함께 정의했다.
- 그리고 크루스칼 알고리즘을 통해 모든 노드를 연결할 수 있는 최소 비용을 구했다.

다만 여전히 서로소 집합에서 노드를 결합(union)할 때 로직이 헷갈렸다.
- 결론: 최상위 부모 노드를 연결해야한다.


대부분의 사람들이 크루스칼 알고리즘이 아닌 힙 구조(or 우선순위 큐)로 문제를 푼 것 같아 해당 방법도 시도해볼 예정이다.

```
"""
격자 칸 안에는 숫자가 있다.
칸의 숫자에는 그 칸의 높이가 있다.

모든 칸이 서로 이동이 가능하도록 만들어야한다.
높이 차가 height를 초과하는 경우 사다리(비용 +높이차)가 발생한다.

최대한 적은 이용으로 사다리를 설치해야한다.

모든 격자가 단일 노드

노드끼리 간선이 있다. 기본 0.
근데 간선을 최소한으로 이어서 모든 노드를 연결해야하는 문제로 바꿀 수 있다.
"""
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def solution(land, height):
    map_height = len(land)
    map_width = len(land[0])
    
    edges = set() # [(비용, 노드A, 노드B)]
    
    def find_node_id(y, x):
        return y * map_width + x
    def make_edge(y, x):
        for dir in dirs:
            new_y = y + dir[0]
            new_x = x + dir[1]
            if new_y < 0 or new_x < 0:
                continue
                
            if new_y >= map_height or new_x >= map_width:
                continue
            
            key = tuple(sorted([
                find_node_id(y,x), find_node_id(new_y,new_x)
            ]))
            cost = abs(land[y][x] - land[new_y][new_x])
            if cost <= height:
                cost = 0
            edges.add((cost, key[0], key[1])) 
    for y in range(map_height):
        for x in range(map_width):
            make_edge(y, x)
    # 최저 비용 순서대로 매핑함.
    edges = sorted(edges)
    parents = [i for i in range(map_height * map_width)]
    
    def find_parent(node):
        if node != parents[node]:
            # 경로 단축
            parents[node] = find_parent(parents[node])
        return parents[node]
    
    def union(a, b): # 확인 필요
        root_a = find_parent(a)
        root_b = find_parent(b)
        parents[root_a] = root_b
 
    answer = 0
    for cost, a, b in edges:
        # A랑 B의 부모가 다르면
        if find_parent(a) != find_parent(b):
            #print(f"{a+1}({find_parent(a) + 1}) 랑 {b+1}({find_parent(b) + 1}) 연결함 {cost}")
            union(a, b)
            answer += cost
            # print(parents)
        
    return answer
```