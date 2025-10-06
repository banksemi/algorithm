https://school.programmers.co.kr/learn/courses/30/lessons/49995

특별한 문제 없음
투포인터 문제

```
def solution(cookie):
    # 나는 m을 오른쪽 사람꺼라고 생각하자.
    def check(m):
        l = m
        r = m
        l_sum = 0
        r_sum = cookie[m]
        answer = 0
        while True:
            if l_sum == r_sum:
                answer = l_sum
                l -= 1
                r += 1
                if l < 0:
                    break
                if r == len(cookie):
                    break
                l_sum += cookie[l]
                r_sum += cookie[r]

            elif l_sum < r_sum:
                l -= 1
                if l < 0:
                    break
                else:
                    l_sum += cookie[l]
            elif l_sum > r_sum:
                r += 1
                if r == len(cookie):
                    break
                else:
                    r_sum += cookie[r]
        return answer
    answer = 0
    for i in range(0, len(cookie)):
        answer = max(answer, check(i))
    return answer
```