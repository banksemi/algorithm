[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/92345

거의 방향은 맞았으나, 문제에서 놓친 1가지 조건이 있었고, 모호해서 생각까지만 하고 구현하지 못했던 부분이 있다.

틀린 부분1: 놓친 조건
- 두 플레이어가 같은 타일에 있으면, 한명이 움직이는 순간 게임은 끝난다.

틀린 부분2: 이동 경로에 따라 승패가 갈리는 케이스가 있다.
- 이때 항상 '승리'를 따라가게 하자. 물론, '승리하는 케이스' 안에서 최소 이동 거리
- 그러면 반대쪽은 어느 순간 '패배' 의 선택지에서만 고르게 되고, 자연스럽게 최대 이동거리를 선택할 수 있다.
- 이 부분이 모호하게 생각이 되서 아래처럼 주석만 남기고 실제 구현을 못했었다.
```
return result[0]
# 하나를 선택할 수 있으면, 당연히 이기는걸 선택한다.
```


```
"""
문제: 두 플레이어가 총 캐릭터를 얼마나 움직였는지 찾자.

움직일때마다 과거 발판이 사라진다.
양 플레이어는 번갈아가면서 상하좌우로 이동한다.

게임 종료 조건
- 이동할 턴에, 주변 4칸 모두 발판이 없거나 보드 밖이면 패배
- 두 캐릭터가 같은 발판에 있으면, 상대가 다른 발판으로 이동하게 되면 발판이 사라지므로 패배

항상 A 부터 시작.

중요한 힌트
- 이길 수 있는 플레이어는 항상 이길려고 한다.
- 지는 플레이어는 항상 오래 버틴다.

이길 수 있는 플레이어?

def dfs
    4 방향으로 이동했을 때 승패 조합을 본다.
    4 방향 중 가장 승률이 높은 것 하나가 이 턴의 승률이 된다.
    항상 이길 수 밖에 없는 플레이어는 100% 승률이 나오는 것이 있을 것이다.
    
보드 조건: 1*1 ~ 5*5 이내
"""
import sys
sys.setrecursionlimit(2*30)

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def reverse(text):
    if text == 'A':
        return 'B'
    else:
        return 'A'
    
def solution(board, aloc, bloc):
    height = len(board)
    width = len(board[0])
    def move_tile(y, x):
        result = []
        for dir in dirs:
            new_y = y+dir[0]
            new_x = x+dir[1]
            if height <= new_y or width <= new_x:
                continue
            if new_y < 0 or new_x < 0:
                continue
            if board[new_y][new_x] == 0:
                continue
            result.append((new_y, new_x))
        return result
    
    def dfs(turn, ayx, byx): # [True, 0(턴수)]
        result = []
        yx = ayx if turn == 'A' else byx
        if not move_tile(yx[0], yx[1]):
            return (reverse(turn), 0)
        else:
            # (내가 틀린 부분 1)
            # 움직일 수는 있는데 ... 다른 상대방이랑 위치가 같으면
            if ayx == byx:
                return (turn, 1)
        for new_y, new_x in move_tile(yx[0], yx[1]):
            board[yx[0]][yx[1]] = 0
            if turn == 'A':
                ayx = (new_y, new_x)
            else:
                byx = (new_y, new_x)
            
            result.append(dfs(reverse(turn), ayx, byx))
            board[yx[0]][yx[1]] = 1
        
        if len(set([i[0] for i in result])) == 1:
            # 전부 내가 이긴거면, 최소 움직임을 선택한다.
            if result[0][0] == turn:
                return (result[0][0], min([i[1] for i in result]) + 1)
            else:
                return (result[0][0], max([i[1] for i in result]) + 1)
        else:
            # (내가 틀린 부분 2) 내가 승리할 수 있는 조건 중 최소를 고른다.
            return (turn, min([i[1] for i in result if i[0] == turn]) + 1)
        # 하나를 선택할 수 있으면, 당연히 이기는걸 선택한다.
        
    return dfs('A', (aloc[0], aloc[1]), (bloc[0], bloc[1]))[1]
```