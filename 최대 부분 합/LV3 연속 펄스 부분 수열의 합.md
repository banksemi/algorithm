https://school.programmers.co.kr/learn/courses/30/lessons/161988

코딜리티에서 풀었던 것 처럼 부분 합을 구하다가, 현재 합이 -가 되면 초기화하는 방식을 사용했다.

DP로 푼 사람들이 많은 것 같아 해당 풀이도 볼 예정.

```
"""
연속 펄스 부분 수열의 합 중 가장 큰 것

최대 부분 합을 카데인 알고리즘으로 풀자.

"""
def solution(sequence):
    # TODO: 펄스 수열 없다고 가정하고 일단 풀기 -> 나중에 펄스 신호 추가
    def run(multiple):
        max_sum = 0
        current_sum = 0
        for value in sequence:
            current_sum += value * multiple
            multiple *= -1
            if current_sum < 0:
                current_sum = 0
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    return max(run(1), run(-1))
```

----
아래는 누적 합으로 푼 케이스
최대 누적 합 - 최소 누적 합 = 최대 부분 합
- NOTE: 단 최소 누적 합은 0일 수 있음 (0번부터 시작하는 부분 수열을 고려)
```
def solution(sequence):
    def run(multiple):
        current_sum = 0
        min_sum = 0 # 아무것도 선택 안하는 경우
        max_sum = -1e9
        for value in sequence:
            current_sum += value * multiple
            multiple *= -1
            
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)
            # 누적합 기준으로 최대 최소를 서로 빼주면 가장 큰 부분 수열이 나온다.
            # min, max를 구하기 전 테이블에 기록하면 -> DP와 유사한 형태가 나온다.
        return max_sum - min_sum
    
    return max(run(1), run(-1))
```