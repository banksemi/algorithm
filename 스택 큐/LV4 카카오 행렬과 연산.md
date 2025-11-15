[틀림, 정답 보고 풀이] https://school.programmers.co.kr/learn/courses/30/lessons/118670
행렬의 바깥 부분을 빠르게 회전시키기 위한 효율성을 다루는 문제

deque가 2차원으로 확장된 케이스를 생각할 수 있어야함

2차 풀이 (left_col, rows, right_col 분리)
```
from collections import deque

def solution(rc, operations):
    left_col = deque([row[0] for row in rc])
    right_col = deque([row[-1] for row in rc])
    rows = deque([deque(row[1:-1]) for row in rc])
    width = len(rc[0])
    height = len(rc)
    def shiftrow():
        left_col.appendleft(left_col.pop())
        rows.appendleft(rows.pop())
        right_col.appendleft(right_col.pop())
        
    def rotate():
        first = left_col.popleft()
        rows[0].appendleft(first)
        right_col.appendleft(rows[0].pop())
        rows[-1].append(right_col.pop())
        left_col.append(rows[-1].popleft())
    def get_result():
        arr = []
        for left, row, right in zip(left_col, rows, right_col):
            arr.append([left] + list(row) + [right])
        return arr
    
    for op in operations:
        if op == 'Rotate':
            rotate()
        else:
            shiftrow()
    return get_result()
```

1차 풀이 (효율성 틀림)
```
"""
효율성 (9개중 3,8 통과)
정확성: 25.0
효율성: 16.7
합계: 41.7 / 100.0

"""
def solution(rc, operations):
    width = len(rc[0])
    height = len(rc)
    def shiftrow():
        nonlocal rc
        rc =  [rc[-1]] + rc[:-1]
    def rotate():
        nonlocal rc
        first = rc[0][0]
        current_dir = 'd'
        y = 1
        x = 0
        while current_dir:
            if current_dir == 'd':
                rc[y-1][x] = rc[y][x] # 전칸에다가 복사해서 넣기
                if y+1 == height: # 더 내려갈 수 없는 경우
                    x += 1
                    current_dir = 'r'
                else:
                    y += 1
                continue
            
            if current_dir == 'r':
                rc[y][x-1] = rc[y][x] # 전칸에다가 복사해서 넣기
                if x+1 == width: # 더 내려갈 수 없는 경우
                    y -= 1
                    current_dir = 'u'
                else:
                    x += 1
                continue
            if current_dir == 'u':
                rc[y+1][x] = rc[y][x] # 전칸에다가 복사해서 넣기
                if y == 0: # 더 내려갈 수 없는 경우
                    x -= 1
                    current_dir = 'l'
                else:
                    y -= 1
                continue
            
            if current_dir == 'l':
                rc[y][x+1] = rc[y][x] # 전칸에다가 복사해서 넣기
                if x == 0: # 더 내려갈 수 없는 경우
                    current_dir = None
                else:
                    x -= 1
                continue
        rc[0][1] = first
    
    for op in operations:
        if op == 'Rotate':
            rotate()
        else:
            shiftrow()
    return rc
```