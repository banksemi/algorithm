최소 비용을 구하는 문제지만 로봇이 벽을 만날때까지 슬라이딩한다는 차이점이 있다.

원하는 값을 찾았을 때, Deque에 넣지 말고 바로 결과를 반환하자.
- 이전에 이것때문에 시간초과가 뜬 적이 있다!

BFS 문제

```
"""

시작 -> 목표에 멈추기 위해 최소 몇번의 이동? 

움직일 수 있는 방향: 상하좌우 한 방향으로 장애물이나 가장자리까지 미끄러지는걸 한번의 이동으로 정의한다.


비용이 1인점을 BFS로 풀자.
"""

from collections import deque

dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

def solution(board):
    visited = [[0] * len(board[0]) for _ in range(0, len(board))]
    
    # find start_point
    queue = deque()
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            if board[y][x] == 'R':
                queue.append((y,x,0))
                visited[y][x] = 1
    
    def slide(y, x, dy, dx):
        while True:
            y += dy
            x += dx
            
            condition1 = x < 0 or y < 0 or y >= len(board) or x >= len(board[0])
            if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]):
                y -= dy
                x -= dx
                return y, x
            if board[y][x] == 'D':
                y -= dy
                x -= dx
                return y, x
        
            
    while queue:
        item = queue.popleft()
        for dy, dx in dirs:
            new_y, new_x = slide(item[0], item[1], dy, dx)
            
            # 이미 방문한 노드는 무시
            if visited[new_y][new_x] == 1:
                continue
            
            # 원하는 값을 찾으면 queue에 넣지 않고 빠른 종료 (효율성)
            if board[new_y][new_x] == 'G':
                return item[2] + 1
            
            visited[new_y][new_x] = 1
            queue.append((new_y, new_x, item[2] + 1))
    return -1
```