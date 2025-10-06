[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/43236
문제가 풀리지 않아 힌트를 받았다.

문제의 경우의 수를 찾기보다, 답을 정해두고 결정 문제로 바꿔서 푸는 연습을 더 해야할 것 같다.

```
"""
0 위치 -> [2, 11, 14, 17, 21] -> 25

문제 단순화
- 결과를 정해두고 그게 되는지 보는 문제로
- "돌 2개를 제거했을 때 최소 값이 4보다 큰게 가능한가?"
-> 돌은 순서대로 가다가. 최소 값이 4 미만이면 돌 강제로 한개씩 제거
n 개 제거할때까지 모든 돌을 스캔했으면 문제가 없음.

def check(target=2): O(n) > 5만
    [2, 11, 14, 17, 21]
    0 -> 11 -> 17, 21...
    OK
    return OK
    ...
"""

def solution(distance, rocks, n):
    rocks.sort()
    def check(target):
        current = 0
        count = n
        for i in rocks:
            if i - current < target:
                count -= 1
                if count == -1:
                    return False
            else:
                current = i
        
        # 마지막도 똑같이 체크해야함
        if distance - current < target:
            if count >= 1:
                return True
            else:
                return False
        return True

    def bsearch(min_i, max_i):
        m = (min_i + max_i) // 2
        if min_i == max_i:
            return min_i
        value = check(m)
        
        if value:
            return bsearch(m+1, max_i)
        else:
            return bsearch(0, m)
    
    return bsearch(0, distance+1) - 1
```