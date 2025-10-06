https://school.programmers.co.kr/learn/courses/30/lessons/12927

특별한 이슈 없음.
- 동일한 work 시간을 모아서 한번에 처리하는 방법 사용

```
"""
1:24 시작 


works: 1~20000개, 5만 이하
n = 1백만

[5,4,3,3]
[5시간, 1개], [4시간, 1개], [3시간 2개]
[4시간, 2개], [3시간 2개]
[3시간 4개]
"""
from collections import deque
def solution(n, works):
    queue = deque()
    temp = {i: 0 for i in range(0, 50001)}
    for i in works:
        temp[i] += 1
    
    keys = sorted(temp.keys(), reverse=True)
    for key in keys:
        queue.append([key, temp[key]])
    while queue:
        item = queue[0]
        if n == 0:
            break
        if item[0] == 0:
            break
        
        # 만약 n이 더 작아질 수 없으면 n 만
        available = min(item[1], n)
        item[1] -= available
        n -= available
        
        queue[1][1] += available
        if item[1] == 0:
            queue.popleft()
            
    answer = 0
    for work, count in queue:
        answer += count * (work ** 2)
    return answer
```