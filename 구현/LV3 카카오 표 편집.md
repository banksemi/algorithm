https://school.programmers.co.kr/learn/courses/30/lessons/81303

Linked List에 대한 구현 문제
- 행을 이동하는 횟수(칸)은 최대 100만으로 제한되어있어 시간 복잡도가 크게 증가하지 않는다.
- 따라서 행의 삭제와 복구를 신경써야하는 문제. (첫번째 행, 마지막 행 제거 케이스 신경쓰기)

```
"""
7:44 시작, 8:16 종료

행 개수 5 ~ 100만
k: 처음 위치: 0 ~ 100만 미만

명령 수: 1~20만개

해결해야할 문제들
- X칸 위로 가기.
- X칸 아래로 가기.
- C 현재 칸 삭제 후, 바로 아래 (마지막행인경우 윗칸)
- Z 복구
위치를 바로 움직일 수 있어야할 것 같다.
행을 삭제하는 로직을 어떻게 떙길까?

X(이동 수)는 1_000_000 이하다. = 즉 이동하는건 한칸에 O(1)이 걸릴 때 문제 없다는 뜻
#그러면 
"""

class Node:
    no: int
    def __init__(self, no):
        self.no = no
        self.previous_node = None
        self.next_node = None
        self.removed = False
        
    def __str__(self):
        return f"Node[{self.no}]"
    
    def is_last(self):
        return self.next_node is None
    
    def remove(self):
        self.previous_node.next_node = self.next_node
        if self.next_node:
            self.next_node.previous_node = self.previous_node
        self.removed = True
    
    def restore(self):
        self.previous_node.next_node = self
        if self.next_node:
            self.next_node.previous_node = self
        self.removed = False
        
    # previous_node
    # next_node
def solution(n, k, cmd):
    init_node = Node(-1)
    last_node = init_node
    selected_node = None
    _fix_tables = []
    for i in range(n):
        node = Node(i)
        _fix_tables.append(node)
        node.previous_node = last_node
        last_node.next_node = node
        if i == k:
            selected_node = node
        last_node = node
    def get_result():
        result = ''
        for node in _fix_tables:
            if node.removed:
                result += 'X'
            else:
                result += 'O'
        return result
            
    def move_down(x):
        nonlocal selected_node
        for i in range(x):
            selected_node = selected_node.next_node
    
    def move_up(x):
        nonlocal selected_node
        for i in range(x):
            selected_node = selected_node.previous_node

    rollback_stack = []
    for command in cmd:
        operator = command[0]
        if operator == 'D':
            move_down(int(command[1:].strip()))
        elif operator == 'U':
            move_up(int(command[1:].strip()))
        elif operator == 'C':
            rollback_stack.append(selected_node)
            if selected_node.is_last():
                move_up(1)
            else:
                move_down(1)
            rollback_stack[-1].remove()
        elif operator == 'Z':
            rollback_stack.pop().restore()

    answer = ''
    return get_result()
```