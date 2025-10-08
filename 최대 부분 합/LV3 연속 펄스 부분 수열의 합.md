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