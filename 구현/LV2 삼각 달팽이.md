
dir로 움직일 방향을 설정하고 움직이면서 해결이 되었다.
다만 n 값이 1인 경우를 고려하지 못해서 오답 처리가 되었다. 나중에 문제를 풀때 꼭 n의 범위를 체크해서 테스트 케이스로 넣자.


```
print = lambda *args, **kwargs: ...
def solution(n):
    answer = [[0] * n for i in range(0, n)]
    
    # 그래프는 y랑 x로 생각하자.
    
    # 아래로 가는거, 오른쪽으로 가는거, 대각선으로 올라가는거
    dirs = [(1, 0), (0, 1), (-1, -1)]
    dir_status = 0
    current_y = 0
    current_x = 0
    
    def allow_move(y, x):
        if y == n or x == n:
            return False
        if y < 0 or x < 0:
            return False
        if answer[y][x] != 0:
            return False
        return True
        ...
        
    for i in range(1, n*n+ 1): # 어차피 조기 종료됨
        # 현재 위치를 채운다.
        
        answer[current_y][current_x] = i
        print("일단 값 채우기 시작")
        # for y in range(0, n):
        #    print(answer[y])
        print("----")
        
        # 다음 목표로 가는 로직을 확인한다.
        current_dir = dirs[dir_status]
        next_y = current_y + current_dir[0]
        next_x = current_x + current_dir[1]
        if allow_move(next_y, next_x):
            current_y = next_y
            current_x = next_x
            continue
            
        # 만약 다음 목표에 값이 있거나 움직일 수 없으면 방향을 바꾸고 움직일 수 있는지 확인한다.
        print("방향을 바꾼다.")
        dir_status = (dir_status + 1) % len(dirs)
        current_dir = dirs[dir_status]
        next_y = current_y + current_dir[0]
        next_x = current_x + current_dir[1]
        
        if allow_move(next_y, next_x):
            current_y = next_y
            current_x = next_x
            continue
        else:
            # 만약 값을 채울 수 없으면
            print("강제 중단", n)
            break
        
    # answer을 평면으로 피자.
    result = []
    for row in answer:
        result.extend([i for i in row if i != 0])
    return result
```