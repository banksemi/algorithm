
A,B의 위치를 tuple 상태로 나타내고 풀이를 진행했다. (이 문제를 풀기 위한 초기 아이디어와 동일)
- 다만 효율성 테스트에서 시간 초과가 발생하여 (a,b) = (b,a)로 생각하는 캐싱을 도입했다.


참고: 이전 풀이는 경유 지점을 n개 중 하나를 선택하고 이동 거리를 확인했음.


```
from collections import defaultdict
from queue import PriorityQueue

def hash_position(position):
    return tuple(sorted(position))
    
def solution(n, s, a, b, fares):
    nodes = defaultdict(list)
    for c, d, cost in fares:
        nodes[c].append((cost, d))
        nodes[d].append((cost, c))
        
    queue = PriorityQueue()
    queue.put((0, (s,s)))
    
    visited = set()
    def get_tiles(cost, position):
        s1, s2 = position
        # 만약 s1, s2가 같으면 여전히 같은 택시를 타고 있음 
        if s1 == s2:
            for add_cost, new_node in nodes[s1]:
                yield cost+add_cost, (new_node, new_node)
        
        # S1이 갈 수 있는 노드 중 자유롭게 이동
        for add_cost, new_node in nodes[s1]:
            yield cost+add_cost, (new_node, s2)
            
        for add_cost, new_node in nodes[s2]:
            yield cost+add_cost, (s1, new_node)

        
    while not queue.empty():
        cost, position = queue.get()
        hash = hash_position(position)
        if hash in visited:
            continue
        visited.add(hash)
        
        if position[0] == a and position[1] == b:
            return cost        
        if position[0] == b and position[1] == a:
            return cost
        
        for new_cost, new_position in get_tiles(cost, position):
            if hash_position(new_position) in visited:
                continue
            queue.put((new_cost, new_position))
    answer = 0
    return answer
```