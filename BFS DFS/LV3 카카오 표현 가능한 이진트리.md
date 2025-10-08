https://school.programmers.co.kr/learn/courses/30/lessons/150367

규칙을 찾고, 구현하는 문제. 

```
"""
16:21 시작 -> 17:00 종료

중요한 힌트?: "노드의 높이는 살펴보는 순서에 영향을 끼치지 않습니다."

더미 노드를 추가하여 자리수를 맞추는게 중요하다.
?그리고 더미 노드를 무조건 1이 고정되어야하는 얘들이 있다.

숫자가 왔다.
-> 몇개의 이진수 자리로 표현할 수 있는지 본다.
# 1개, 3개, 7개, 15개... 로 표현해야한다. 앞에 0을 붙여서 가본다.
# 해당 이진 트리가, 정상적인지 본다.
    # 포화 이진트리 -> 모든 잎의 개수가 동일함. -> 더미에서 더미도 가능, 더미에서 1이 나올 수 없음
    
"""

def number_to_bin(number):
    ramain = str(number % 2)
    if number // 2 == 0:
        if number % 2 == 0:
            return ""
        else:
            return "1"
    return number_to_bin(number // 2) + ramain

def reformat_bin(bin_str):
    n = len(str(bin_str))
    for i in range(1, 10000):
        target = 2 ** i - 1
        if n == target:
            return bin_str
        if n > target:
            continue
        if n < target:
            return '0' * (target - n) + bin_str

def dfs(number, min_i, max_i, only_dummy, root) -> bool: # 트리 구성 가능 여부
    m = (min_i + max_i) // 2
    current_str = number[m]
    if only_dummy and current_str == '1':
        return False
    if root and current_str == '0':
        return False
    if min_i + 1 == max_i:
        return True
    
    next_dummy = current_str == '0'
    if not dfs(number, min_i, m, next_dummy, False):
        return False
    if not dfs(number, m+1, max_i, next_dummy, False):
        return False
    return True

def solution(numbers):
    answer = []
    for number in numbers:
        number_str = reformat_bin(number_to_bin(number))
        if dfs(number_str, 0, len(number_str), False, True):
            answer.append(1)
        else:
            answer.append(0)
    return answer
```