---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/1843
문제 유형:
  - DP(Top-down)
풀이 날짜: 2025-11-20
정답 여부: 오답
틀린 이유:
  - 코딩 실수
마지막 풀이 날짜:
---
'+', '-'로 이루어진 수식에서 연산 순서에 따른 최대 값을 찾는 문제.

연산자 기준으로 두 그룹(하위 문제)로 나누어 연산하고 값을 결합하는 방식 (topdown)을 사용함.
- 상황에 따라 '최대 값'이 필요한 경우도 있고 '최소 값'이 필요한 경우도 있어 두 케이스를 모두 구현.

단 마지막에 value 초기 값 설정을 잘못 넣어(-INF 대신 0으로 입력) 오류 발생.


```
"""
6:04
6:22 (77.8점, 오답으로 인한 감점)
-와 +가 있는 배열에서, 계산 결과 최대 값

arr 는 3 이상 201 이하 (숫자는 100 이하인듯)

반으로 나눠서 최대한 특정 케이스를 구하는 문제?
근데 최대한 +하는 경우 최대한 - 하는 경우 둘다 생각하자.

"""
from functools import lru_cache
import sys
INF = 10**30
sys.setrecursionlimit(2**30)
def solution(arr):
    for i in range(0, len(arr), 2):
        arr[i] = int(arr[i])
    
    @lru_cache(maxsize=None)
    def dfs(min_i, max_i, want_max):
        if min_i + 1 == max_i:
            return arr[min_i]
        value = 0
        if want_max == False:
            value = INF
        else:
            value = -INF
        
        func = max if want_max else min
        for i_op in range(min_i+1, max_i, 2):
            if arr[i_op] == '+':
                value = func(value, dfs(min_i, i_op, want_max) + dfs(i_op+1, max_i, want_max))
            else:
                value = func(value, dfs(min_i, i_op, want_max) - dfs(i_op+1, max_i, not want_max))

        return value
    return dfs(0, len(arr), True)
```



```
"""
6:04
6:22 (77.8점, 오답으로 인한 감점)
-와 +가 있는 배열에서, 계산 결과 최대 값

arr 는 3 이상 201 이하 (숫자는 100 이하인듯)

반으로 나눠서 최대한 특정 케이스를 구하는 문제?
근데 최대한 +하는 경우 최대한 - 하는 경우 둘다 생각하자.

"""
from functools import lru_cache
import sys
INF = 10**30
sys.setrecursionlimit(2**30)
def solution(arr):
    for i in range(0, len(arr), 2):
        arr[i] = int(arr[i])
    
    @lru_cache(maxsize=None)
    def dfs(min_i, max_i, want_max):
        if min_i + 1 == max_i:
            return arr[min_i]
        value = 0
        if want_max == False:
            value = INF
        else:
            value = -INF
        
        func = max if want_max else min
        for i_op in range(min_i+1, max_i, 2):
            if arr[i_op] == '+':
                value = func(value, dfs(min_i, i_op, want_max) + dfs(i_op+1, max_i, want_max))
            else:
                value = func(value, dfs(min_i, i_op, want_max) - dfs(i_op+1, max_i, not want_max))

        return value
    return dfs(0, len(arr), True)
```