https://school.programmers.co.kr/learn/courses/30/lessons/42897

연습 문제.

```
"""
0번집을 털면 -> 1번집을 못턴다.

dp[i] = max(dp[i-2] + money, dp[i-1])

# 순환 구조이므로 두 케이스로 나누자
0번 집을 털었을 때, 털지 않았을 때로 시작하자.
- 0번 집을 털었을 때에는 1번은 못털고 2번부터 시작, n-1번 집은 항상 털 수 없다.
- 0번 집을 안털었을 때에는 1번부터 털 수 있고, n-1번 집도 털 수 있다.
"""
def solution(money):
    # money
    n = len(money)
    def case(attack_0):
        nonlocal n
        dp = [0] * n
        if attack_0:
            dp[0] = money[0]
            dp[1] = money[0]
            n = n - 1# 마지막 집은 못턴다.
        else: # 0번 집을 안털었을 때
            dp[0] = 0
            dp[1] = money[1]
        for i in range(2, n):
            dp[i] = max(dp[i-2] + money[i], dp[i-1])
        
        return max(dp)
    answer = 0
    return max(case(False), case(True))
```