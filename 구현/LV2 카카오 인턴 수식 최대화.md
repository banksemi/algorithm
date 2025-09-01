https://school.programmers.co.kr/learn/courses/30/lessons/67257#
[틀림]
문제 마지막에 if문 들여쓰기로 인해 3개의 오답이 발생했다.

만약 코드가 길어질 것으로 예상되는 경우 함수를 통해 관리하자.

```
from itertools import permutations
import copy
print = lambda *args, **kwargs:...
def solution(expression):
    answer = 0
    expression += '+'
    
    temp_num = ''
    _queue = []
    for i in expression:
        if i in ['*', '+', '-']:
            _queue.append([int(temp_num), i])
            temp_num = ''
        else:
            temp_num += i
    for ops in permutations(['*', '+', '-'], 3):
        print(ops)
        queue = copy.copy(_queue)
        for op in ops:
            print(queue)
            i = 0
            while i+1 < len(queue): #마지막은 항상 +이므로 무시

                if queue[i][1] == op:
                    # 뒤에거랑 합치기
                    first = queue[i][0]
                    second = queue[i+1][0]
                    result = None
                    if op == '+':
                        result = first + second
                    if op == '-':
                        result = first - second
                    if op == '*':
                        result = first * second
                    queue[i] = [result, queue[i+1][1]]
                    queue.pop(i+1)
                    print("업데이트", queue)
                else:
                    i += 1
            
        if answer < abs(queue[0][0]):
            answer = abs(queue[0][0])
        print("-------------")
    return answer
 ```