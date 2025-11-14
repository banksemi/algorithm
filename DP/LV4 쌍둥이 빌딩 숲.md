[틀림, 힌트 확인함] https://school.programmers.co.kr/learn/courses/30/lessons/140105

문제 조건에 제약 조건이 명시되어있다.
- 같은 높이의 빌딩은 2개씩 존재하며,
- 같은 높이를 가지는 빌딩 사이에는 그보다 높은 빌딩이 존재하지 않는다.

일단 작은 건물을 우선으로 배치해보는 방식으로 풀었는데, 큰 건물부터 배치하는 내용은 잘 이해가 되지 않아서 확인해볼 예정

```
"""
9:53 시작

높이 제한: 1~ 100
count(구분되어 보이는 빌딩 수): 1<= 빌딩 수 <=n
결과 산출 방식
- 1,000,000,007 으로 나눈 나머지

가장 작은 빌딩을 앞에 세운 경우, 다른 가장 작은 빌딩은 붙어있어야한다. 
- 같은 높이를 가지는 빌딩 사이에는 그보다 높은 빌딩이 존재하지 않는다
- n과 count를 1 감소시킬 수 있다
- dfs(n-1, count-1)


가장 작은 빌딩이 앞에 오지 않은 경우 (n은 감소시키지만, count는 감소시킬 수 없다 작은 블럭은 어디든 갈 수 있다.)
- dfs(n-1, count) * (2*n-2)
- 가장 앞에 오는 경우를 빼고 2*(n-1) 에서 생각

"""
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(n, count):
    if n == 0:
        if count == 0:
            return 1
        else:
            return 0
    result = 0
    
    # 작은 빌딩이 가장 앞에 오는 경우
    result += dfs(n-1, count-1)
    
    # 작은 빌딩이 가장 앞에 오지 않는 경우
    result += dfs(n-1, count) * (2*n-2)
    return result % 1_000_000_007
    
def solution(n, count):
    answer = 0
    return dfs(n,count)
```



Bottom-up
```
def solution(n, count):
    answer = 0
    dp = {}
    dp[(0,0)] = 1
    for i in range(1, n+1):
        dp[(0, i)] = 0
    
    for c in range(1, count+1):
        for i in range(0, n+1):
            if i == 0:
                dp[(c, i)] = 0
            else:
                dp[(c, i)] = (dp[(c-1, i-1)] + dp[(c, i-1)] * (2*i-2)) % 1_000_000_007
        
    return dp[(count, n)]
```