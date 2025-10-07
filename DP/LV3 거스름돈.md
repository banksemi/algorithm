[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/12907
2025-10-07 문제 다시 풀기 진행

정답 보고 해결
거스름돈의 경우의 수를 구하는 DP 문제 
- 1차원 DP로도 풀 수 있지만 2차원으로 풀었다.
- 가능한 가짓수를 한가지씩 늘려보면서 고려하자
	- 배낭 문제처럼


```
"""
거슬러 줘야 하는 금액 n (10만 이하)

화폐 단위 (100종류 이하)
"""
def solution(n, money):
        old_dp = [0] * (n+1)
        new_dp = [0] * (n+1)

        for m in money:
            old_dp = new_dp
            new_dp = [0] * (n+1)
            for i in range(0, n+1):
                if i < m:
                    new_dp[i] = old_dp[i]
                elif i == m:
                    new_dp[i] = old_dp[i] + 1
                else:
                    new_dp[i] = old_dp[i] + new_dp[i - m]

        return new_dp[n] % 1_000_000_007
```