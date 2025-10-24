https://school.programmers.co.kr/learn/courses/30/lessons/388352
n과 m이 제한적이므로 완전 탐색을 통해 후보군을 줄이는 풀이를 선택했다.

```
"""
4:41 4:49 완료
"""
from itertools import combinations
def solution(n, q, ans):
    candidates = [set(arr) for arr in combinations(range(1, n+1), 5)]
    
    for query, result in zip(q, ans):
        candidates = [arr for arr in candidates if len(arr & set(query)) == result]

    return len(candidates)
```
