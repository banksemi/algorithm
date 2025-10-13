[틀림]

더블 슬라이드로 양 쪽의 sum을 합하는 문제인데 X, Z를 보면 선택 지점은 제외하게 된다.
즉 sum의 최소는 0이라는 사실을 기억하자. (양쪽 sum에서)

```
"""
N개의 정수로 구성된 비어 있지 않은 배열 A가 주어졌습니다.

0 ≤ X < Y < Z < N인 삼중항(X, Y, Z)을 이중 슬라이스 라고 합니다 .

더블 슬라이스(X, Y, Z)의 합 은 A[X + 1] + A[X + 2] + ... + A[Y - 1] + A[Y + 1] + A[Y + 2] + ... + A[Z - 1]의 합계입니다.

예를 들어, 다음과 같은 배열 A는 다음과 같습니다.

A[0] = 3 A[1] = 2 A[2] = 6 A[3] = -1 A[4] = 4 A[5] = 5 A[6] = -1 A[7] = 2
content_copy
다음 예제 이중 슬라이스가 포함되어 있습니다.

더블 슬라이스(0, 3, 6), 합은 2 + 6 + 4 + 5 = 17입니다.
더블 슬라이스(0, 3, 7), 합은 2 + 6 + 4 + 5 - 1 = 16,
더블 슬라이스(3, 4, 5), 합은 0입니다.
목표는 임의의 더블 슬라이스의 최대 합의 값을 찾는 것입니다.

함수를 작성하세요:

def solution(A)
content_copy

N개의 정수로 구성된 비어 있지 않은 배열 A가 주어졌을 때, 모든 더블 슬라이스의 최대 합계를 반환합니다.

예를 들어, 다음이 주어졌다면:

A[0] = 3 A[1] = 2 A[2] = 6 A[3] = -1 A[4] = 4 A[5] = 5 A[6] = -1 A[7] = 2
content_copy
배열 A의 이중 슬라이스의 합이 17보다 큰 경우는 없으므로 함수는 17을 반환해야 합니다.

다음 가정에 대한 효율적인 알고리즘을 작성하세요 .

N은 [ 3 .. 100,000 ] 범위 내의 정수입니다 .
배열 A의 각 요소는 [ -10,000 .. 10,000 ] 범위 내의 정수입니다 .
"""

"""
이건 어떻게 풀지?

A: 앞에서부터 N까지의 누적합(근데 만약에 새로 시작하는게 낫다고 생각이 되면 새로 시작하자.)
B: 뒤에서부터 N까지의 누적합 (근데 만약에 새로 시작하는게 낫다고 생각이 되면 새로 시작하자.)

그리고 N 앞뒤로 A,B를 보고 max를 갱신하자. n번 반복
"""
def solution(A):
    front_sum = [0] * len(A)
    back_sum = [0] * len(A)

    # front_sum[0] = A[0]
    # back_sum[-1] = A[-1]
    for i in range(1, len(A)):
        new_sum = front_sum[i - 1] + A[i]

        if new_sum < A[i]:
            new_sum = A[i]
        front_sum[i] = max(0, new_sum)


    for i in range(len(A) - 2, -1, -1):
        new_sum = back_sum[i + 1] + A[i]

        if new_sum < A[i]:
            new_sum = A[i]
        back_sum[i] = max(0, new_sum)
    
    result = None
    for i in range(1, len(A) - 1):
        front = front_sum[i-1]
        back = back_sum[i+1]
        temp = front + back
        if result is None or result < temp:
            result = temp
    return result
```


