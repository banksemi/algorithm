특정 수열의 면적 합을 빠르게 구하는 문제.

누적합은 DP 문제였다.

그리고 사다리꼴 면적 구하기도 한번 고민해보면 좋겠다.
- 그냥 직관적으로 네모, 세모 부분을 구했는데 (윗변+아랫변) * 높이 / 2도 가능하다.

```
"""
a 부터 n-b 구간까지의 면적의 합
만약 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간 -> 정적분 결과는 -1
- 똑같으면 0인것 같다.

구간 연산을 최적화하기 위해 누적 합을 구해두고 사용하자.
"""
def collatz(k):
    yield k # 초항 포함
    while k != 1:
        if k % 2 == 0:
            k //= 2
            yield k
        else:
            k = k * 3 + 1
            yield k

def solution(k, ranges):
    # k에 대해 누적합을 먼저
    points = [i for i in collatz(k)]
        
    prefix_sum = [0] * len(points) # 0부터 x번째 점까지의 면적 합
    
    for i in range(1, len(points)):
        area = 0
        
        # 두 점의 공통 사각형
        area += min(points[i], points[i-1])
        area += (max(points[i], points[i-1]) - min(points[i], points[i-1])) / 2
        prefix_sum[i] = prefix_sum[i-1] + area
        
    answer = []
    for a, b in ranges:
        x1 = a
        x2 = len(points) + b - 1 # n은 k가 초항인 우박수열이 1이 될때 까지의 횟수를 의미
        if x1 == x2:
            answer.append(0)
        elif x1 > x2:
            answer.append(-1)
        else:
            answer.append(prefix_sum[x2] - prefix_sum[x1])
    return answer
```