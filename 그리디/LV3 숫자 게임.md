https://school.programmers.co.kr/learn/courses/30/lessons/12987

2개의 배열과 포인터를 가지고 while으로 풀었다. 
카카오 셔틀버스 문제랑 비슷하게 풀었는데, 나중에 셔틀버스 문제도 다시 풀어봐야겠다.

```
"""
N명씩 두 팀 (A, B)

무작위 자연수,
- 각 경기당 한 사원씩 나와 서로 수 공개, 숫자 크면 이김, 비김도 있음

A 팀의 출전 순서를 정했다.
B팀이 가장 많이 이기는 방향으로 출전 순서를 만들어서 싸워야한다.

패배할 때 감점이 없고, A 팀의 점수를 고려하지 않기 때문에 패배랑 무승부는 비슷하다.
"""


def solution(A, B):
    # 최대한 근접하게 이긴다
    # 지거나 
    A.sort()
    B.sort()
    
    current_a = 0
    current_b = 0
    answer = 0
    while True:
        if len(A) == current_a:
            break
        if len(B) == current_b:
            break
        a = A[current_a]
        b = B[current_b]
        if b > a:
            answer += 1
            current_a += 1
            current_b += 1
        else:
            current_b += 1
            
    return answer
```