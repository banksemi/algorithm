---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/12983
문제 유형:
  - DP(Bottom-up)
풀이 날짜: 2025-12-05
정답 여부: 오답
틀린 이유:
  - 시간 초과
마지막 풀이 날짜:
---
DP를 사용하여 최적화를 했다고 생각했지만 시간 초과 제한이 매우 짧게 설정되어 오답 처리되었다.

추가적인 최적화를 해야했는데 100개의 문자열 비교를 줄일 수 있는 방안을 찾아야한다.
- 문자열 길이는 1에서 5이므로 1,2,3,4,5 각 길이별로 set을 사용하여 O(1)로 찾을 수 있으면 시간을 크게 단축시킬 수 있다.


틀린 버전 (효율성)
```
"""
4:35
가진 단어 사전에서 목적 t를 만들어야한다.

최소 횟수로 만들 수 있는 수를 반환해야한다.

만약 만들 수 없으면 -1을 반환.

변수
- 배열 1~100개, 중복 없음, 1~5의길이가 있음.
- 완성 문자열은 1-20000 이하

DP 문제?
- 특정 구간까지의 최소 카운트를 구한다.
- 모든 단어에 대해 n-len()을 고려해서 업데이트한다.


"""

INF = 99999
def solution(strs, t):
    dp = [INF] * 20_000 # n번째 글자까지 가능한 가지수
    for word in strs:
        if t[0:len(word)] == word:
            dp[len(word)-1] = 1

    for i in range(0, 20_000):
        if dp[i] == INF:
            continue
        # i 번째 단어까지는 완료되어있음.
        for word in strs:
            # i+1번째부터 word만큼이 동일한지 확인
            if t[i+1:i+1+len(word)] == word:
                # i+1 + word - 1 에 갱신
                target = i+len(word)
                dp[target] = min(dp[target], dp[i] + 1)

    answer = dp[len(t)-1]
    if answer == INF:
        return -1
    return answer
```

정답 풀이
```

INF = 99999
def solution(strs, t):
    dp = [INF] * 20_000 # n번째 글자까지 가능한 가지수
    words = set(strs)
    for word in strs:
        if t[0:len(word)] == word:
            dp[len(word)-1] = 1

    for i in range(0, 20_000):
        if dp[i] == INF:
            continue
        # i 번째 단어까지는 완료되어있음.
        for j in range(1, 6):
            t_word = t[i+1:i+1+j]
            if len(t_word) != j:
                break
            if t_word in words:
                target = i+j
                dp[target] = min(dp[target], dp[i] + 1)
    answer = dp[len(t)-1]
    if answer == INF:
        return -1
    return answer
```