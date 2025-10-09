[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/92344
2025-10-09 다시 풀기

2차원 누적합을 사용한 개념
- make_prefix_sum()처럼 y 합계, x 합계를 별도로 계산해야한다.

```
def solution(board, skill):
    width = len(board[0])
    height = len(board)
        
    board_offset = [[0] * width for _ in range(height)]
    def debug(table):
        for arr in table:
            print(arr)
        print("------------")
    
    def _add_offset(y, x, add_value):
        if y >= height or x >= width:
            return False
        if y < 0 or x < 0:
            return False
        board_offset[y][x] += add_value
        return True
    def apply_skill(y1, x1, y2, x2, offset):
        _add_offset(y1, x1, offset)
        _add_offset(y2, x1, -offset)
        _add_offset(y1, x2, -offset)
        _add_offset(y2, x2, offset)
        
    def make_prefix_sum():
        for y in range(height):
            for x in range(width):
                if x != 0:
                    board_offset[y][x] = board_offset[y][x-1] + board_offset[y][x] 
        
        for y in range(height):
            for x in range(width):
                if y != 0:
                    board_offset[y][x] = board_offset[y-1][x] + board_offset[y][x]
                    
    for skill_type, y1, x1, _y2, _x2, degree in skill:
        value = degree
        y2 = _y2 + 1
        x2 = _x2 + 1
        if skill_type == 1:
            value *= -1
        apply_skill(y1, x1, y2, x2, value)
        
    make_prefix_sum()
    
    answer = 0
    for y in range(height):
        for x in range(width):
            if board[y][x] + board_offset[y][x] > 0:
                answer += 1
    return answer
```
---
아래는 틀린 풀이들

1차 풀이 (틀림)
- 기본적으로는 skill이 올때마다 보드를 갱신한다.
- 효율성을 위해 변경해야할 타일 수가 > 전체/2를 초과하면, 반대 부분을 칠하도록 했으나, 여전히 worst case를 커버할 수 없다.
```
"""
보드 길이: 최대 1000 * 1000
내구도: 각각 1000 이하
skill: 1 부터 250,000 개
보드 칸수: 1,000,000
"""
import numpy

        
def solution(board, skill):
    offset = 0
    height = len(board)
    width = len(board[0])
    
    half_count = height * width / 2
    
    def _commit(y1, x1, y2, x2, degree):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                board[y][x] += degree
    def use_skills(skill_one):
        nonlocal offset
        degree = skill_one[-1]
        if skill_one[0] == 1:
            degree *= -1
        
        y1, x1, y2, x2 = skill_one[1:5]
        effect_nodes = (y2-y1+1) * (x2-x1+1)
        if effect_nodes < half_count:
            _commit(y1, x1, y2, x2, degree)
        else:
            # 역전해서 더 효율적인 방법을 찾는다.
            if y1 > 0: # 0을 포함하지 않는 경우 윗부분 커버
                _commit(0, 0, y1 - 1, width - 1, -degree)
            
            if y2 != height-1: # 마지막을 포함하지 않는 경우 아래 커버
                _commit(y2+1, 0, height-1, width - 1, -degree)
            
            if x1 > 0:
                _commit(y1, 0, y2, x1 - 1, -degree)
            if x2 != width-1:
                _commit(y1, x2+1, y2, width - 1, -degree)
            offset += degree
    
    for s in skill:
        use_skills(s)
    
    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] + offset >= 1: # 1 이상
                answer += 1
    return answer
```


2차 풀이 (틀림)
- 힌트를 보고 누적합을 적용했다. 다만 2차원 누적 합이 와닿지 않아 1차원 누적합으로 접근했다.
- 세로로 긴 스킬들이 많을 때 여전히 비효율적 로직을 수행하게 되는 한계가 있다.

```
"""
보드 길이: 최대 1000 * 1000
내구도: 각각 1000 이하
skill: 1 부터 250,000 개
보드 칸수: 1,000,000
"""
import numpy

        
def solution(board, skill):
    height = len(board)
    width = len(board[0])
    
    skill_board = [[0] * width for i in range(height)]
    def use_skills(skill_one):
        degree = skill_one[-1]
        if skill_one[0] == 1:
            degree *= -1
        
        y1, x1, y2, x2 = skill_one[1:5]
        for y in range(y1, y2 + 1):
            skill_board[y][x1] += degree
            if x2 != width - 1: # 끝 부분이 아니라면
                skill_board[y][x2 + 1] -= degree # 다음 노드부터는 원상복구
                
        
        
    
    for s in skill:
        use_skills(s)
    
    # 누적합을 사용해서 스킬 보드 갱신
    for y in range(height):
        for x in range(width):
            if x > 0:
                skill_board[y][x] = skill_board[y][x - 1] + skill_board[y][x]
    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] + skill_board[y][x] >= 1: # 1 이상
                answer += 1
    return answer
```


3차