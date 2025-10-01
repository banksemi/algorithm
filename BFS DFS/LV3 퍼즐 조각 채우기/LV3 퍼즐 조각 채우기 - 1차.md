https://school.programmers.co.kr/learn/courses/30/lessons/84021

BFS 문제, 과거에는 못풀었지만 이번엔 풀렸다!

구현 문제다. 문제를 단계적으로 나눠서 생각해보자.
- 퍼즐을 2차원 배열로 관리하지 않고 1차원 배열로 (y,x)가 담기게 한게 나쁘지 않았다.

퍼즐의 인접한 포인트가 다 막혔는지 보려면, 그냥 퍼즐 위에서 dirs을 통해 전부 하나씩 확인해보면 된다. (BFS랑 원리 동일)


```
"""
조각: 한번에 하나, 회전 가능, 뒤집기는 불가, 새로 채워넣을 때 인접한 칸이 비어있으면 안됌 (모두 막혀있어야함)


칸을 스캔하면서 (왼쪽 오른쪽 -> 한칸 아래)
넣을 수 있는 조각을 찾고(회전 고려), 넣을 수 있으면 -> 후보에서 빼고 나머지 DFS, 


일단 퍼즐 조각들을 분리해 내는 작업

퍼즐을 회전해보는 작업

각 퍼즐+회전 -> 들어갈 수 있는 공간이 있는지 탐색, 들어갈 수 있으면 거기 그냥 들어가기, 순서 상관없음 (인접 칸 비어있기X, 하나씩 정책때문에)
"""

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
from collections import deque

def trim_plz(plz):
    # 0,0에서 시작하게 만들어주기
    min_y = min([i[0] for i in plz])
    min_x = min([i[1] for i in plz])
    return [(i[0] - min_y, i[1] - min_x) for i in plz]

def rotate_90(plz):
    # 0, 1, 2
    # 3, 4, 5
    # 6, 7, 8
    # 9, 10, 11
    
    # 9, 6, 3, 0
    # 10, 7, 4, 1
    # 11, 8, 5, 2
    
    # (4,1) -> (1, 0)
    
    # (0,0) -> (x) (height - y - 1)
    
    height = max([i[0] for i in plz]) # 이거 사실 필요없음 trim_plz 덕분에 잘 돌아감
    return trim_plz([(x, -y - 1) for y, x in plz])
    
def solution(game_board, table):
    height = len(game_board)
    width = len(game_board[0])
    plzs = []
    
    def split_plz(y, x):
        queue = deque([(y,x)])
        result = []
        while queue:
            item = queue.popleft()
            y = item[0]
            x = item[1]
            if table[y][x] == 0:
                continue
            table[y][x] = 0
            result.append(item)
            for dir in dirs:
                y = item[0] + dir[0]
                x = item[1] + dir[1]
                if x < 0 or y < 0:
                    continue
                if x >= width or y >= height:
                    continue
                if table[y][x] == 0:
                    continue
                queue.append((y, x))
        return trim_plz(result)
    
    # 퍼즐 분리하기
    plzs = []
    for y in range(height):
        for x in range(width):
            if table[y][x] == 1:
                plzs.append(split_plz(y,x))
                
    def match_plz(start_y, start_x, plz):
        # 먼저 퍼즐의 1 영역이 다 들어가는지 확인
        # plz 는 0,0보다 항상 큼
        for plz_y, plz_x in plz:
            target_y = start_y + plz_y
            target_x = start_x + plz_x
            if target_y >= height:
                return False
            if target_x >= width:
                return False
            
            if game_board[target_y][target_x] == 1:
                return False
        # 1영역이 다 들어가면 일단 테이블을 채워두기
        for plz_y, plz_x in plz:
            target_y = start_y + plz_y
            target_x = start_x + plz_x
            game_board[target_y][target_x] = 1
        
        # 채워두고 1영역에서 dirs 4방향이 전부 막혔는지 확인
        error = False
        for plz_y, plz_x in plz:
            target_y = start_y + plz_y
            target_x = start_x + plz_x
            for dir in dirs:
                y = target_y + dir[0]
                x = target_x + dir[1]
                # 영역을 초과하는건 괜찮음
                if y < 0 or x < 0:
                    continue
                if y >= height or x >= width:
                    continue
                if game_board[y][x] == 0: # 비어있는건 안됌
                    error = True
                    break
        if error:
            # 안막혔으면 복구하고 False
            for plz_y, plz_x in plz:
                target_y = start_y + plz_y
                target_x = start_x + plz_x
                game_board[target_y][target_x] = 0
            return False
        else:
            return True
    
    answer = 0
    for y in range(height):
        for x in range(width):
            for plz_no in range(len(plzs)):
                plz = plzs[plz_no]
                matched = False
                for _ in range(4):
                    if match_plz(y, x, plz):
                        matched = True
                        break
                    plz = rotate_90(plz)
                    
                if matched:
                    answer += len(plz)
                    plzs.pop(plz_no)
                    break
    return answer
```