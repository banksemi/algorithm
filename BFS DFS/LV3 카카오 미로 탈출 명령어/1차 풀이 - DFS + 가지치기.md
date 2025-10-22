[다른 방법으로 다시 풀어보기] https://school.programmers.co.kr/learn/courses/30/lessons/150365
이 문제는 이전에 풀이를 살짝 본적이 있다. 물론 DFS 방법은 아니었지만, 이를 통해 # 가지치기 2 힌트를 생각할 수 있었다.

다양한 풀이 방법이 있기 때문에 다시 풀어볼 필요가 있다.
- 가지치기 2 대신 lru_cache를 적용할 경우 마지막 테스트케이스(약 9초, limit=10초)정도로 통과된다.

```
"""
7:24 시작
7:39 완료

50, 50, k=2500
"""
import sys
sys.setrecursionlimit(2**30)
def get_distance(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x2 - x1)
dirs_char = ['d', 'l', 'r', 'u']
dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
def solution(n, m, x, y, r, c, k):
    height = n
    width = m
    start_y = x - 1
    start_x = y -1
    target_y = r - 1
    target_x = c - 1
    # height = 50
    # width = 50
    # k = 100000
    def get_tile(y, x):
        for char, iyx in zip(dirs_char, dirs):
            new_y = y + iyx[0]
            new_x = x + iyx[1]
            if new_y < 0 or new_x < 0:
                continue
            if new_y == height or new_x == width:
                continue
            yield char, new_y, new_x
            
    def dfs(y, x, remain_k):
        # 가지치기 1
        if get_distance(y, x, target_y, target_x) > remain_k:
            return None
        
        # 가지치기 2 (중요)
        if get_distance(y, x, target_y, target_x) % 2 != remain_k % 2:
            return None
        if target_y == y and target_x == x and remain_k == 0:
            return []
        
        for char, new_y, new_x in get_tile(y, x):
            result = dfs(new_y, new_x, remain_k-1)
            if result is not None:
                return [char] + result
    result = dfs(start_y, start_x, k)
    if result is None:
        return 'impossible'
    return ''.join(result)
```