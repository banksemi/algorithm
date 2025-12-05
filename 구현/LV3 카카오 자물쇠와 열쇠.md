---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/60059
문제 유형:
  - 구현
  - 완전 탐색
풀이 날짜: 2025-12-05
정답 여부: 정답
틀린 이유:
마지막 풀이 날짜:
---
문제를 읽고 완전 탐색으로 시간 내 실행이 가능한지 확인하여 풀었다. 한번 비교할때 20\*20의 연산이 수행되며, -20~+20의 y,x 구간을 모두 탐색해야한다.

```
"""
3:10 시작
3:31 완료
좌물쇠를 푸는 문제.

열쇠는 회전과 이동 가능.

키를 돌리고 이동시켜서 홈을 맞춰야함.
- 영역을 벗어나면 그 부분은 무시할 수 있음

홈 0, 돌기 1

최대 크기 20

비교할때 20*20영역을 60*60(offset)으로 탐색
- 영역 밖에서 순차적으로 영역을 완전히 초과할때까지 탐색
회전은 4방향 이니까 *4
총 144만 * 4으로 해결 가능

생각해봐야할거
- 키가 더 큰경우
- 보드가 더 큰경우
"""

def solution(key, lock):
    target_count = 0 # 돌기로 채워야하는 횟수
    for row in lock:
        for i in row:
            if i == 0:
                target_count += 1
    print(target_count)
    def rotate(board):
        # 시계 방향으로 90도 회전하는 코드
        size = len(board) # 정사각형 가정
        new_board = [[0] * size for _ in range(size)]
        for y in range(size):
            for x in range(size):
                new_board[x][size-y-1] = board[y][x]
        return new_board
    
    def check(y_offset, x_offset):
        size = len(key) # 정사각형 가정
        board_size = len(lock)
        count = 0 # 보드 돌기로 채워야하는 횟수
        for _y in range(size):
            for _x in range(size):
                board_y = _y + y_offset
                board_x = _x + x_offset
                if board_y < 0 or board_x < 0:
                    continue
                if board_y >= board_size or board_x >= board_size:
                    continue
                # 일치하는 영역 사이에서는 모두 확인해야한다.
                if key[_y][_x] == lock[board_y][board_x]:
                    return False
                if lock[board_y][board_x] == 0:
                    count += 1
        if count != target_count:
            return False
        return True
            
    for _ in range(4):
        key = rotate(key)
        for y_offset in range(-20, 21):
            for x_offset in range(-20, 21):
                if check(y_offset, x_offset):
                    return True
    
    return False
```