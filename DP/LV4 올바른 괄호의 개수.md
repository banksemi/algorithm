https://school.programmers.co.kr/learn/courses/30/lessons/12929

DP 문제로 접근.

근데 지금 DP 문제를 풀 때 계속 Top-down 방식으로 풀게 되는 것 같다.
문제를 분할하는 DFS 구조를 만들고 캐싱을 메모이제이션을 적용하고 있지만, Bottom-up 방식도 공부해야할 것 같다.

```
from functools import lru_cache
def solution(n):
    answer = 0
    @lru_cache(maxsize=None)
    def dfs(value, opened):
        if value == 0:
            if opened == 0:
                return 1
            else:
                return 0
        
        # print({"value": value, "opened": opened})
        # value가 여유가 있을 때
        result = 0
        
        # 닫아보기
        if opened > 0:
            result += dfs(value - 1, opened - 1)
            
        # 열어보기
        result += dfs(value - 1, opened + 1)
        return result
        
    return dfs(n * 2, 0)
```