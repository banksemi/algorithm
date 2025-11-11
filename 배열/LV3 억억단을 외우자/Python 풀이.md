[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/138475
1. 마지막에 'starts'는 정렬되어있다는 가정이 없기 때문에 answers 생성시 순서를 고려해야했다.
2. Python에서 시간 초과가 발생했는데, 반복문 내의 불필요한 if 구문을 제거하는 방식으로 최적화. (참고: Java에서 풀 경우 8~9초 걸리던 코드가 1초 이내로 완료됨)

```
"""
1:19 시작, 1:48 (틀림: 사유 starts의 순서가 달라질 경우 answers 순서를 바꿔야함)

e 이하의 임의의 수 s 여러개

s보다 크거나 같고, e보다 작거나 같은 수 중 표에서 가장 많이 등장한 수
- 여러개면 가장 작은 수

[1, 8]
- 
1: 1
2: 1 3
3: 1,3
4: 1,2,4
5: 1,5
6: 1,2,3,6
7: 1,7
8: 1,2,4,8
~ 5_000_000까지

5_000_000까지 소수만 판단하는 알고리즘

DP: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]...
소수만 사용해서 DP에 반복 더하기

1 세기 
1: [[1,[1]],[2,[2,3,5,7]]]
"""

MAX_NUMBER = 5_000_000#16
def solution(e, starts):
    MAX_NUMBER = e
    dp = [0] * (MAX_NUMBER+1)
    for i in range(1, MAX_NUMBER+1):
        for j in range(i, MAX_NUMBER+1, i):
            dp[j] += 1
    current_max = e
    answer = []
    cache = {}
    wants = set(starts)
    for i in range(e, 0, -1):
        
        if dp[current_max] <= dp[i]:
            current_max = i
        if i in wants:
            cache[i] = current_max
        
    return [cache[s] for s in starts]
```
