---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/42895
문제 유형:
  - DP(Bottom-up)
풀이 날짜: 2025-11-20
정답 여부: 정답
틀린 이유:
마지막 풀이 날짜: 2025-11-20
---
```
"""
4:55 시작, 5:08 완료

n과 사칙 연산을 사용해서 number를 달성할 수 있는 가장 최소 n 사용 수 반환
"""
def get_combination(count): # 3 -> (1,2) (2,1) 반환
    result = []
    for i in range(1, count):
        result.append((i, count - i))
    return result

def solution(N, number):
    dp = [set() for i in range(0, 9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

    if number == N:
        return 1
    
    all_values = set() # 여기에 들어간건 포함하지 않음 (이미 더 적은 수의 조합에서 해결 가능)
    def try_add(target_count, value):
        if value in all_values:
            return
        all_values.add(value)
        dp[target_count].add(value)
        
    for target_count in range(2, 9):
        for i, j in get_combination(target_count):
            for i_number in dp[i]:
                for j_number in dp[j]:
                    try_add(target_count, i_number + j_number)
                    try_add(target_count, i_number - j_number)
                    try_add(target_count, i_number * j_number)
                    if j_number != 0:
                        try_add(target_count, i_number // j_number)

        for i in dp[target_count]:
            if number == i:
                return target_count

    return -1
```