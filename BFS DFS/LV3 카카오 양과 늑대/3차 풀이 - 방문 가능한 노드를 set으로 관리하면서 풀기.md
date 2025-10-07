https://school.programmers.co.kr/learn/courses/30/lessons/92343

DFS 탐색 문제를 다시 풀어봤다. 이번에는 'available'이라고 갈 수 있는 경로를 표시해둔 set 자료구조를 사용한다.

'가지치기'
- 이번에 문제 조건 중 '양이 늑대에게 잡아먹히지 않고' 라는 힌트가 있다. 처음에는 잡아 먹혀도 더 나은 경로가 있지 않을 까 했는데, 실제로는 늑대가 하나라도 있으면 양을 모으는게 불가능하다. 즉 가지치기 조건이다.

'반복문에서 배열 값을 조작하는 경우를 조심하자'
- 반복문을 돌리고 있는 배열 의 요소를 조작하면 오류가 발생된다. 근데 반복문 배열의 개수를 유지하면 동작은 하는 경우가 있다. 이 경우 파이썬 버전에 따라 예상치 못한 동작으로 이어질 수 있기 때문에, copy를 통해 얕은 복사 후 사용하자. 

```
"""
양의 수 <= 늑대 가 되면 양이 모두 잡아먹힌다.

1. 양이 잡아 먹히지 않게 하라.
2. 최대한 많은 수의 양을 모아라
def dfs(현재 노드, 양, 늑대)
"""

def solution(info, edges):
    answer = 0
    nodes = {}
    for i in range(len(info)):
        nodes[i] = []
    for i, j in edges:
        nodes[i].append(j)
        
    available = set()
    answer = 0
    def dfs(parent, a, b):
        nonlocal answer
        if info[parent] == 0:
            a += 1
        else:
            b += 1
        if a <= b: # 양보다 늑대가 많거나 같으면 (문제의 조건이기도 하고 가지치기 조건이기도 하다. 늑대가 있으면 양이 바로 잡아먹혀 양을 모을 수가 없다.)
            return
        answer = max(answer, a)
        # 아래에 있는 2개의 자식 노드를 후보에 추가한다.
        for i in nodes[parent]:
            available.add(i)
        
        # 현재 상황에서 갈 수 있는 모든 노드를 확인한다.
        # 주의: set을 변형하는 것은 파이썬 동작에 오류가 날 가능성이 높다. 복사해서 쓰자.
        for i in available.copy():
            available.remove(i)
            dfs(i, a, b)
            available.add(i)
        
        for i in nodes[parent]:
            available.remove(i)
    dfs(0, 0, 0)
    return answer
```