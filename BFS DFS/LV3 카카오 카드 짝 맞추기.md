https://school.programmers.co.kr/learn/courses/30/lessons/72415

구현 + 백트래킹 문제

풀긴 했으나, 구현 과정에서 시간이 많이 쓰였다. (약 42분)
순서를 구하는 부분을 permutations으로 풀려다가 DFS으로 전환했는데 이 부분에서 구현 소요 시간을 줄여야할 것 같다.

```
"""
구현 문제 (11:18분 시작) (12:00 종료)
def 좌표이동 (현재y, 현재x, 목표y, 목표x) -> 키보드 누름 개수:
    이걸 할때 카드 상태를 보고 컨트롤 키를 고려해야함.
    
def 카드 읽는 순서 정하기
카드_(번호)_(1or2) 들이 있는데, 어떤 순서로 찾아갈지 확인
목표 도달시 엔터 한번씩 포함해야함
def 현재 좌표->
"""
# from queue import PriorityQueue
from collections import deque
from copy import deepcopy
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(board, r, c):
    height = len(board)
    width = len(board[0])
    
    def check_tile_available(y, x):
        if y < 0 or x < 0:
            return False
        if y >= height or x >= width:
            return False
        return True
    
    def get_tiles(y, x):
        for iy, ix in dirs:
            new_y = y
            new_x = x
            for i in range(100):
                new_y += iy
                new_x += ix
                if not check_tile_available(new_y, new_x):
                    # 갈 수 없으면 벽이라도 가야할지 아니면 끝나는지 정해야함
                    if i == 0:
                        break
                    elif i == 1: # 다시 본인 자리로 돌아올수는 없다.
                        break
                    else:
                        new_y -= iy
                        new_x -= ix
                        yield new_y, new_x
                        break
                # 갈수 있으면서 카드 만나면 그거까지는 가고, 마무리
                if i == 0:
                    yield new_y, new_x
                    # 마침 카드였다면 끝.
                    if board[new_y][new_x] != 0:
                        break
                else:
                    if board[new_y][new_x] != 0:
                        yield new_y, new_x
                        break
                
    def move(start_y, start_x, target_y, target_x):
        queue = deque()
        queue.append((0, start_y, start_x)) # 비용이 항상1이다.
        visited = [[False] * width for i in range(height)]
        while queue:
            cost, y, x = queue.popleft()
            if visited[y][x]:
                continue
            visited[y][x] = True
            if y == target_y and x == target_x:
                return cost
            # 갈 수 있는 노드 (물론 비용은 1이다)
            for new_y, new_x in get_tiles(y, x):
                if visited[new_y][new_x]: #가지치기
                    continue 
                queue.append((cost+1, new_y, new_x))
        raise Exception("런타임 오류")
    
    # 방문할 카드 순서 정하기
    cards = {}
    for y in range(height):
        for x in range(width):
            if board[y][x] != 0:
                number = board[y][x]
                if number not in cards:
                    cards[number] = []
                cards[number].append((y, x))
    
    need_cards = set(cards.keys())
    def dfs(y, x):
        if not need_cards:
            return 0
        result = 1e9
        for i in need_cards.copy():
            for left, right in [(cards[i][0], cards[i][1]), (cards[i][1], cards[i][0])]:
                # 왼쪽 먼저 방문하는 경우
                card1 = left
                card2 = right
                score = 0

                score += move(y, x, card1[0], card1[1])
                board[card1[0]][card1[1]] = 0

                score += move(card1[0], card1[1], card2[0], card2[1])
                board[card2[0]][card2[1]] = 0

                need_cards.remove(i)
                score += dfs(card2[0], card2[1])

                # 복구
                need_cards.add(i)
                board[card1[0]][card1[1]] = i
                board[card2[0]][card2[1]] = i
                result = min(result, score)
        return result
    return dfs(r, c) + len(cards) * 2
```