https://school.programmers.co.kr/learn/courses/30/lessons/42895
사칙 연산 DP 문제.

기억이 잘 안났다. DP 문제를 여러번 풀어봐야할 것 같다.
또한 최소 값 (N=1) 같은 시나리오도 꼭 테스트 케이스에 포함하자.


```
"""
사칙 연산

N은 1~9
number: 32000 이하 (작네)

최대 8개의 N을 사용할 수 있음.
"""

def solution(N, number):
    dp = {
        i: set([int(str(N) * i)]) for i in range(1, 9)
    }
    
    # 중요: 항상 최소 값을 꼭 체크하자
    if N == number:
        return 1
    for target_n in range(2, 9):
        for n2 in range(1, target_n):
            n3 = target_n - n2 # n2 n3로 target_n을 만드는 모든 경우의 수 

            for value1 in dp[n2]:
                for value2 in dp[n3]:
                    if value2 != 0:
                        dp[target_n].add(value1 // value2)
                    dp[target_n].add(value1 + value2)
                    dp[target_n].add(value1 - value2)
                    dp[target_n].add(value1 * value2)
        
        # target_n 번의 조합은 이제 확정됨 -> 결과 확인 가능
        if number in dp[target_n]:
            return target_n
    return -1
```