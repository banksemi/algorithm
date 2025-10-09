https://school.programmers.co.kr/learn/courses/30/lessons/131129

맞긴 했지만, dp[점수]가 아닌 dp[횟수, 싱글 카운트]로도 접근이 가능한지 확인 필요.

```
"""
가능한 가지수
1~20: 싱글 
2,4,6...40: 더블
3,6,9...60: 트리플
불: 50

가장 먼저 0점을 만들기
- 1. 가장 적은 횟수
- 2. 가장 적은 횟수 내에서는 '싱글'과 '불'을 사용한 조합으로 만들기

DP 문제?
- 1~20, 불을 사용해서 먼저 DP 테이블을 만들어준다. DP[점수] 테이블에는 (횟수, -(싱글+불))이 함께 존재한다.
"""

def solution(target):
    MAX_SCORE = 100_000
    dp = [(0, 0)] * (MAX_SCORE+1)

    def update_dp(m, is_single):
        for i in range(m, (MAX_SCORE+1)):
            new = (dp[i-m][0] + 1, dp[i-m][1] - (1 if is_single else 0))
            if dp[i][0] == 0:
                dp[i] = new
            else:
                dp[i] = min(new, dp[i])
    
    for i in range(1, 21):
        update_dp(i, True)
        update_dp(i * 2, False)
        update_dp(i * 3, False)
    update_dp(50, True)
    return (dp[target][0], -dp[target][1])
```