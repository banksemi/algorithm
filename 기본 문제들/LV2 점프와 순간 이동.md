https://school.programmers.co.kr/learn/courses/30/lessons/12980

```
"""
기능
- 점프: K 칸을 앞으로 점프한다. (건전지 소모량 K 발생)
- 순간이동: 현재까지 온 거리 * 2로 순간이동한다.

문제:
- 건전지 사용량을 최소로 하는 방법 근데 n 지점에 정확히 도착해야한다.

n은 1 이상 10억 이하 (DP가 어려울 수도)

그리디?
어쨌든 처음엔 한칸 이동해야한다.
그리고 최대한 순간 이동으로 간다.

반절 이하에서만 가능하다.


1칸 이동 후 순간이동 2,4,8
1,2,3,6,

"""

def solution(n):
    ans = 0
    used = 0
    position = n
    while position > 0:
        if position % 2 == 1:
            position -= 1
            used += 1
            continue
        # 순간이동이 가능하면
        position /= 2

    return used
```