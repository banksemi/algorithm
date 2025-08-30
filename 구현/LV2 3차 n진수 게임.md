https://school.programmers.co.kr/learn/courses/30/lessons/17687

n진수 변환하는 과정에서 너무 많은 시간이 소요되었다. 이런건 빠르게 구현하는 스피드를 기르자.
총 걸린 시간: 30분

```
from collections import deque
print = lambda *args, **kwargs:...
number_map = {}

for i, s in enumerate('0123456789ABCDEF'):
    number_map[i] = s
    
def change_str(number, n) -> str:
    if number == 0:
        return '0'
    if number < n:
        return number_map[number]
    a = number // n
    b = number % n
    result = ''
    if a != 0:
        result += change_str(a, n)
    result += number_map[b]
    return result

def split(string) -> deque:
    result = deque()
    for i in string:
        result.append(i)
    return result


def solution(n, t, m, p):
    # n: 진법
    # t: 미리 구할 숫자 개수
    # m: 참가 인원
    # p: 순서 (1 = 첫번째)
    p = p - 1 # 0을 첫번째로 만든다.
    original_number = 0
    current = deque()
    answer = []
    i = -1
    while True: # TODO: 이거 바꿔야함
        i += 1
        # 말할 값이 없으면
        if len(current) == 0:
            current = split(change_str(original_number, n))
            original_number += 1
            # 만들고 original_number을 1 더해둔다.
        if len(current) == 0:
            print("오류", current)
            return ''
        char = current.popleft()
        if (i % m == p):
            print("내 차례", char)
            answer.append(char)
        else:
            print("안함", char)
        
        if len(answer) == t:
            return ''.join(answer)
    answer = ''
    return answer
```