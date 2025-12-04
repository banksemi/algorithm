---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/42894
문제 유형:
  - DFS
  - 구현
풀이 날짜: 2025-12-05
정답 여부: 오답
틀린 이유:
  - 논리 오류
마지막 풀이 날짜:
---
먼저 문제를 풀었을때 블럭이 사라지는 경우 해당 영역을 검은 블럭으로 채웠다.
그러나 블럭이 사라진 자리에 항상 검은 블럭을 채울 수 있는 것이 아니었기 때문에 오답 판정이 나왔다.

또한 두 블럭이 결합되고 하나의 검은 블럭으로 동시에 직사각형을 만들 수 있는 경우가 있지 않을까 생각이 들었다. 사실 이 부분은 여전히 모호한 부분 중 하나.
- https://school.programmers.co.kr/questions/13392

틀린 후 수정한 코드
```
"""
3:39 시작
4:11 10/100

상황
- 판에 블럭이 배치되어있다.

문제
- 크기가 1인 블럭을 위에서 떨어뜨려 완전한 직사각형을 만들 수 있으면 블럭을 없앨 수 있다.

주어지는 변수
- board: 4~50 크기의 2차원 배열
- 이 안에는 0빈칸, 최대 200의 블럭 정보가 있음.

구해야하는 것
- 없앨 수 있는 블록의 최대 개수

생각해야하는거
- 두 블럭이 합쳐져서 직사각형을 만드는 경우를 고려해야하는가?

전략
- 먼저 검은 블럭으로 채울 수 있는 영역은 전부 검은색으로 칠한다.
- 만약 없앨 수 있는 개별 블럭이 있으면 answer +=1 하고 해당 블럭을 다시 검은색으로 칠한다.
"""

dirs = [(0, -1), (0, 1), (1,0), (-1,0)]
def solution(board):
    height = len(board)
    width = len(board[0])
    
    

    
    
    def get_tiles(y, x):
        for iy, ix in dirs:
            new_y = y + iy
            new_x = x + ix
            if new_x < 0 or new_y < 0:
                continue
            if new_x >= width or new_y >= height:
                continue
            yield new_y, new_x
            
    def remove(y, x):
        block_number = board[y][x]
        if block_number <= 0:
            return False, None
        visited = set()
        
        def dfs(y, x):
            if (y,x) in visited:
                return 
            
            visited.add((y,x))
            
            for new_y, new_x in get_tiles(y,x):
                if board[new_y][new_x] == block_number:
                    dfs(new_y, new_x)
        dfs(y,x)
        
        for new_y in range(min([i[0] for i in visited]), max([i[0] for i in visited])+1):
            for new_x in range(min([i[1] for i in visited]), max([i[1] for i in visited])+1):
                if board[new_y][new_x] != block_number and board[new_y][new_x] != -1:
                    return False, None
        
        for y, x in visited:
            if board[y][x] == block_number:
                board[y][x] = 0
        return True, min([i[0] for i in visited])
    
    def fill():
        for x in range(width):
            for y in range(0, height):
                if board[y][x] <= 0:
                    board[y][x] = -1
                else:
                    break
    
    answer = 0
    y = 0
    fill()
    while y < height:
        retry_condition = False
        for x in range(width):
            result, move_y = remove(y,x)
            if result:
                answer += 1
                y = move_y
                retry_condition = True
                fill()
                continue
        if not retry_condition:
            y += 1
    print(board)
    return answer
```