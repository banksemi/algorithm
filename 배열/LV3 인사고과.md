---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/152995
문제 유형:
  - 배열
  - 정렬
풀이 날짜: 2025-12-26
정답 여부: 오답
틀린 이유:
  - 논리 오류
마지막 풀이 날짜:
---
푸는데 시간이 오래 걸리고 채점시 오답이 많이 발생한 문제. 인센티브를 제외할 사용자를 효과적으로 골라내는 방법이 필요하다. 나중에 꼭 다시 풀어볼 것.

```
"""
1:00

변수
- scores: [근무 태도 점수, 동료 평가 점수] 0번째는 완호의 점수

인센티브를 받지 못하는 경우 -1을 return

점수의 합을 사용하여 등수를 매긴다.
- 동점 처리 - 공동 1등, 2등 없음 (여러명도 고려해야함)

풀이
일단 인센티브를 받지 못하는 사용자를 모두 걸러야한다.
두 점수가 모두 낮은 경우가 있으면
"""
def solution(scores):
    # 직무 태도 관점에서 가장 높은 점수를 가진 사용자를 뽑는다.
    scores = sorted([(i, value[0], value[1]) for i, value in enumerate(scores)], key=lambda x: (-x[1], -x[2]))
    current = None
    base_line = None
    new_scores = []
    for i, x, y in scores:
        if current is None:
            current = (x,y)
        if current[0] > x:
            base_line = current
        if current[1] < y:
            current = (x,y)
        if current[0] > x:
            base_line = current
        if not base_line or base_line[0] <= x or base_line[1] <= y:
            new_scores.append((i, x+y))
    new_scores.sort(key=lambda x: -x[1])
    answer = 0
    i = 0
    answer_score = None
    for no, score in new_scores:
        if answer_score is None or answer_score != score:
            answer_score = score
            answer = i + 1
        if no == 0:
            return answer
        i += 1
            
    return -1
```