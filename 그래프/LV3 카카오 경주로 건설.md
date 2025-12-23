---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/67259
문제 유형:
  - 다익스트라
풀이 날짜: 2025-12-23
정답 여부: 정답
틀린 이유:
마지막 풀이 날짜:
---
특별한 이슈 없음.

```
"""
12:48, 12:58 종료
"""
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
import heapq
def solution(board):
    N = len(board)
    def get_tiles(y, x):
        for iy, ix in dirs:
            new_y = y + iy
            new_x = x + ix
            if new_y < 0 or new_x < 0:
                continue
            if new_y >= N or new_x >= N:
                continue
            if board[new_y][new_x] == 1:
                continue
            yield new_y, new_x
    answer = 0
    queue = [(0, 0, 0, (1, 0)), (0, 0, 0, (0, 1))] # 좌측 or 하단으로 시작
    visited = set()
    while queue:
        cost, y, x, dir = heapq.heappop(queue)
        if (y,x,dir) in visited:
            continue
        visited.add((y,x,dir))
        if y == N-1 and x == N-1:
            return cost
        for new_y, new_x in get_tiles(y, x):
            new_dir = (new_y - y, new_x - x)
            new_cost = cost + 100
            if dir != new_dir:
                new_cost += 500
            if (new_y, new_x, new_dir) not in visited:
                heapq.heappush(queue, (new_cost, new_y, new_x, new_dir))
    return answer
```