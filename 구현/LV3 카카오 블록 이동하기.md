https://school.programmers.co.kr/learn/courses/30/lessons/60063

로봇이 90도씩 회전할 수 있고, 중심 축은 고정되지 않았다는 점에서 디버그 시간(13분)이 소요됨.
- 회전 로직을 실수가 나오지 않게끔 작성할 수 있는 다른 풀이가 있는지 확인 예정


```
"""
11:00 시작, 디버깅 11:20, 완료 11:33
로봇은 90도 회전 가능성이 있음
- 세로일때 가로, 가로일때 세로
- 회전 조건: 회전 방향에 벽이 없어야함
- 회전 시간: 1초
단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다
이동 시간: 1초

통과 조건
: 로봇이 차지하는 두 칸중 어느 한칸이라도 N,N 위치에 도달
: 필요한 최소 시간 반환

가정
- 로봇이 처음 있는 칸은 항상 0이며, 목적지에 도착할 수 있다고 가정
- board 한 변의 크기 5 ~100

맵: 0-길, 1-벽

풀기
- 로봇의 베이스는 항상 왼쪽 위, 
"""
from collections import deque
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def solution(board):
    N = len(board)
    height = len(board)
    width = len(board[0])
    # 특정 타일이 이동 가능한지=벽이 아닌지 확인

    def available_single_tile(y, x):
        if y < 0 or x < 0:
            return False
        if y >= height or x >= width:
            return False
        if board[y][x] == 1:
            return False
        return True
    def get_sub_position(y, x, status_to_right):
        if status_to_right: # 오른쪽을 향하고 있으면
            return (y, x+1)
        else: #아래를 향하고 있으면
            return (y+1, x)
    def get_tiles(y, x, status_to_right): # (y,x, status_to_right)
        result = []
        for iy, ix in dirs:
            new_y = y + iy
            new_x = x + ix
            sub_y, sub_x = get_sub_position(new_y, new_x, status_to_right)
            if status_to_right: # 오른쪽을 향하고 있으면
                sub_y = new_y
                sub_x = new_x + 1
            else: #아래를 향하고 있으면
                sub_y = new_y + 1
                sub_x = new_x
            if available_single_tile(new_y, new_x) and available_single_tile(sub_y, sub_x):
                result.append((new_y, new_x, status_to_right))
        return result
    def get_rotate_tiles(y, x, status_to_right):
        result = []
        if status_to_right:
            # 경유지점 + 최종 지점 
            if available_single_tile(y+1, x) and available_single_tile(y+1, x+1):
                result.append((y, x+1, not status_to_right))
                result.append((y, x+0, not status_to_right))
            
            if available_single_tile(y-1, x) and available_single_tile(y-1, x+1):
                result.append((y-1, x+1, not status_to_right))
                result.append((y-1, x+0, not status_to_right))
        else:
            # 최종 지점 + 경유 지점
            if available_single_tile(y, x+1) and available_single_tile(y+1, x+1):
                result.append((y, x, not status_to_right))
                result.append((y+1, x, not status_to_right))
            
            if available_single_tile(y, x-1) and available_single_tile(y+1, x-1):
                result.append((y, x-1, not status_to_right))
                result.append((y+1, x-1, not status_to_right))
        return result
    
    def is_finished(y, x, status_to_right):
        sub_y, sub_x = get_sub_position(y, x, status_to_right)
        if y == N-1 and x == N-1:
            return True
        if sub_y == N-1 and sub_x == N-1:
            return True
        return False
    queue = deque()
    queue.append((0, 0, 0, True)) #cost, y, x, status_to_right

    visited = set()
    while queue:
        cost, y, x, status = queue.popleft()
        key = (y,x,status)
        if key in visited:
            continue
        
        visited.add(key)
        if is_finished(y, x, status):
            return cost
        for new_y, new_x, new_status in get_tiles(*key)+get_rotate_tiles(*key):
            new_cost = cost+1
            new_key = (new_y, new_x, new_status)
            if new_key in visited:
                continue
            queue.append((new_cost, new_y, new_x, new_status))
```