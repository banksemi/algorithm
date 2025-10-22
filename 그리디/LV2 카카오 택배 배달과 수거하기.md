https://school.programmers.co.kr/learn/courses/30/lessons/150369

택배 배달 시뮬레이션 문제, 가장 먼 거리에 있는 택배는 언젠가 방문해야하므로 해당 위치부터 배달을 시도한다.

N은 10만인데, 다음 배달 위치를 효율적으로 파악할 수 있도록 deque를 통해 배달 위치를 관리했다.

```
"""
집: 1부터 N번까지 있음. 각 거리는 1
트럭: cap개 실을 수 있음.

5:45 시작, 6:04 완료
remains = deque((i, count))
"""

def move(remains, available):
    position = None
    while available and remains:
        temp = min(remains[0][1], available)
        if position is None:
            position = remains[0][0]
        remains[0][1] -= temp
        available -= temp
        if remains[0][1] == 0:
            remains.popleft()
    return position

from collections import deque
def solution(cap, n, deliveries, pickups):
    case1 = deque()
    case2 = deque()
    for i in range(n-1, -1, -1):
        if deliveries[i]:
            case1.append([i+1, deliveries[i]])
        if pickups[i]:
            case2.append([i+1, pickups[i]])

    position = 0
    cost = 0
    while case1 or case2:
        position = 0
        if case1:
            position = move(case1, cap)
            cost += position
        if case2:
            new_position = move(case2, cap)
            cost += abs(position - new_position)
            position = new_position
        cost += position
    return cost
```