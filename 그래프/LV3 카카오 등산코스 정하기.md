[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/118669
풀이 방향은 맞았으나, 다익스트라 종료 조건을 잘못 판단하여 오답 판정이 났다. (24/25)

모든 출발지에서 출발했을 때, 가장 쉼터를 거치면서 가장 적은 cost로 봉우리를 찍고 돌아오는 문제다.

가장 적은 cost로 이동해서 봉우리를 찍는다면, 그대로 돌아올 수 있기 때문에 '최단 경로'로 1개 이상의 봉우리를 찾는 문제로 바꿀 수 있다.

다만 시작 지점이 한개가 아니며, 도착 지점도 여러 개가 될 수 있는데 플로이드워셜 알고리즘은 시간 초과 판정이 발생하기 때문에 사용하기 어렵다.

따라서 다익스트라를 응용하여 문제를 풀었다.
- 우선순위 큐에 모든 출발지를 넣고 탐색을 시작하여, 가장 빠르게 도착 가능한 봉우리를 찾는다.
- 단 쉼터를 방문이라는 예외가 있기 때문에 max(이전 코스트, 새로운 코스트)를 사한다.
- 이 조건에 따라 봉우리를 찾았더라도 같은 코스트로 도달 가능한 더 작은 번호의 봉우리가 나타날 수 있기 때문에 탐색을 이어가야한다.
	- cost가 항상 증가하는 케이스에서는 탐색을 이어가지 않아도 되지만, 이 문제에서는 이동을 해도 cost가 변하지 않는 경로들이 많다.

```
"""
11:50 시작

지점 1~n
- 출입구, 쉼터, 산봉우리 중 하나

등산로
- 양방향, cost 있음

intensity
- 쉼터 혹은 산봉우리 방문할 때마다 휴식이 가능한데, 휴식 없이 이동해야하는 가장 긴 시간

출입구 중 하나에서 출발해서, '산봉우리 한번', '출입구는 처음과 끝에 한번씩' = 원래의 출입구로 돌아오기
- 그러면서 intensity가 최소가 되어야함.


양방향이니까 단순히 출입구에서 산봉우리까지 가는거만 생각해도 된다.
- 중간에 만나는 출입구는 단순히 쉼터다.
- 봉우리를 처음 발견하는데, 특히 번호가 가장 작은 경우 완료
- 즉 cost가 똑같은 상황이 있을 수 있음을 인지해야한다.

다익스트라를 쓰되, 약간의 변형
- 시작 지점을 여러 군데에서 동시에 출발시킨다. 이 과정에서 cost가 증가(최대값)하는 것을 고려하자.
- 이미 방문한 노드는 신경쓰지 않는다. (우선순위 큐를 통해 최소로 방문했기 때문에)
12:00

96.8점 12:11
답안 확인 후 수정 12:23
"""
from collections import defaultdict
from heapq import heappush, heappop, heapify
def solution(n, paths, gates, summits):
    nodes = defaultdict(list)
    for i, j, w in paths:
        nodes[i].append((w, j)) # COST, 경로
        nodes[j].append((w, i))
        
    is_gate = set(gates)
    is_summits = set(summits)
    
    # 모든 출발지를 한번에 고려한다.
    queue = [(0, i) for i in gates]
    heapify(queue) # TODO
    
    visited = set()
    found_result = None
    while queue:
        cost, node = heappop(queue)
        if found_result is not None and found_result[0] < cost:
            break
            
        if node in visited:
            continue
        visited.add(node)
        
        # 방문한 노드가 봉우리면
        if node in is_summits:
            # 잘못 생각한 부분
            # - w는 항상 1보다 크다 -> 움직일때마다 최소 1 소요되기 때문에 같은 cost에 새로운 봉우리 후보가 등장하지 않는다.
            # - 따라서 queue에 있는 봉우리끼리만 비교하면 되는데, node 번호가 우선순위 큐의 조건으로 작동하기 때문에 항상 빠른 번호의 봉우리임이 확인된다.
            # 실제로는 같은 cost의 새로운 봉우리가 추가될 수 있다 -> cost를 더하지 않고 max만 사용하기 때문에
            if found_result is None or found_result > (cost, node):
                found_result = (cost, node)
            continue
        for next_cost, next_node in nodes[node]:
            if next_node in visited or next_node in is_gate:
                continue
                
            next_cost = max(cost, next_cost) # 출발지는 어차피 cost가 0
            heappush(queue, (next_cost, next_node))
    answer = []
    return (found_result[1], found_result[0])
```