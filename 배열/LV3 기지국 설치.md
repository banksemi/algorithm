---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/12979
문제 유형:
  - 배열
  - 구간 병합
  - 그리디
  - 선형 탐색
풀이 날짜:
정답 여부: 오답
틀린 이유:
  - 코딩 실수
마지막 풀이 날짜:
---

풀이
전파 닿는 범위를 구간으로 만들어서 배열을 효과적으로 사용.
이때 전파가 겹치는 구간은 병합.
전파가 닿지 않은 구간만 확인 후 기지국 설치.

틀린 이유
need 변수가 0인 경우 반복문을 스킵했는데, last 변수의 업데이트가 함께 스킵되면서 오류 발생.

```
"""

그리디 접근

범위 압축 (전파가 닿는 범위를 [[a, b], [a,b]...])


"""
from collections import deque
from math import ceil
def solution(n, stations, w):
    answer = 0
    
    cover = deque([])
    for i in stations:
        a = max(1, i - w)
        b = min(n, i + w)
        if cover:
            if cover[-1][1] >= a-1:
                cover[-1][1] = b
            else:
                cover.append([a,b])
        else:
            cover.append([a,b])

    last = 0
    answer = 0
    if not cover or cover[0][0] != 1:
        cover.appendleft([0,0])
    if not cover or cover[-1][1] != n:
        cover.append([n+1, n+1])
    for a, b in cover:
        need = a - last - 1
        answer += ceil(need / (2*w + 1))
        last = b
    return answer
```


```
정확성  테스트

|   |   |
|---|---|
|테스트 1 〉|통과 (0.01ms, 9.25MB)|
|테스트 2 〉|통과 (0.01ms, 9.4MB)|
|테스트 3 〉|통과 (0.02ms, 9.19MB)|
|테스트 4 〉|통과 (0.03ms, 9.14MB)|
|테스트 5 〉|통과 (0.02ms, 9.39MB)|
|테스트 6 〉|통과 (0.02ms, 9.26MB)|
|테스트 7 〉|통과 (0.02ms, 9.33MB)|
|테스트 8 〉|통과 (0.01ms, 9.3MB)|
|테스트 9 〉|통과 (0.02ms, 9.33MB)|
|테스트 10 〉|통과 (0.02ms, 9.38MB)|
|테스트 11 〉|통과 (0.01ms, 9.21MB)|
|테스트 12 〉|통과 (0.02ms, 9.29MB)|
|테스트 13 〉|통과 (0.02ms, 9.32MB)|
|테스트 14 〉|통과 (0.02ms, 9.05MB)|
|테스트 15 〉|통과 (0.01ms, 9.29MB)|
|테스트 16 〉|통과 (0.02ms, 9.3MB)|
|테스트 17 〉|통과 (0.03ms, 9.29MB)|
|테스트 18 〉|통과 (0.02ms, 9.32MB)|
|테스트 19 〉|통과 (0.04ms, 9.32MB)|
|테스트 20 〉|통과 (0.02ms, 9.26MB)|
|테스트 21 〉|통과 (0.03ms, 9.32MB)|

효율성  테스트

|   |   |
|---|---|
|테스트 1 〉|통과 (7.11ms, 10.2MB)|
|테스트 2 〉|통과 (9.00ms, 10.7MB)|
|테스트 3 〉|통과 (7.79ms, 10.3MB)|
|테스트 4 〉|통과 (8.78ms, 10.5MB)|
```