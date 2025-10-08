[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/92344

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


2차 

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