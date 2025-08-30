
https://school.programmers.co.kr/learn/courses/30/lessons/12946#

하노이의 탑, 처음에는 생각이 안났는데 답을 직접 구해보면서 특징이 보였다.

n=1일때 [1,3]
n=2일때 [1,2], [1,3] , [2,3]
n=3일때 [1,3], [1,2], [3,2], [1,3], [2,1], [2,3], [1,3]

즉 기존 n-1의 원판을 2 지점으로 옮기고, 마지막 원판을 3 지점으로 옮기고 복구하는 알고리즘.

이걸 a, b, 그리고 빈 공간 c로 나눠서 함수를 만들었다.

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