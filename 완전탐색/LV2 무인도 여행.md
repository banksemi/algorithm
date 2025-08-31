https://school.programmers.co.kr/learn/courses/30/lessons/154540

재귀 함수 호출 제한으로 인해 런타임 에러가 발생했다.

1. 꼭 최댓값을 확인하자.
2. setrecursionlimit 을 잊지 말자.

```
import sys

sys.setrecursionlimit(1_000_000)
dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]

def solution(maps):
    temp = []
    for y in range(0, len(maps)):
        temp.append([i for i in maps[y]])
    maps = temp
    y_n = len(maps)
    x_n = len(maps[0])
    # maps[y][x]
    def dfs(y, x) -> int: # 얻을 수 있는 식량 반환
        # 방문 할수 있으면 방문해서 합치기
        # 그리고 X 표시
        # 방문 할 수 없으면 0 반환
        if x < 0 or y < 0:
            return 0
        if x >= x_n or y >= y_n:
            return 0
        
        if maps[y][x] == 'X':
            return 0
        
        value = int(maps[y][x])
        maps[y][x] = 'X'
        for iy, ix in dirs:
            value += dfs(y+iy, x+ix)
        return value
    
    answer = []
    for y in range(0, len(maps)):
        for x in range(0, len(maps[y])):
            value = dfs(y, x)
            if value > 0:
                answer.append(value)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
```