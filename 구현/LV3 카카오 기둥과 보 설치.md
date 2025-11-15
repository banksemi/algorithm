https://school.programmers.co.kr/learn/courses/30/lessons/60061

기둥과 보를 설치할 수 있는 조건을 함수로 옮겼다.
같은 위치에 기둥과 보가 동시에 존재할 수 있고, 이를 효율적으로 관리하기 위해 set을 사용.

특정 위치의 보나 기둥을 삭제했을 때, 구조물이 유지되는지 조건은 간단한 백트래킹 사용
- 강제로 특정 위치의 기둥이나 보 빼기
- 연결된 구조물이 모두 조건을 만족하는지 확인
- 하나라도 만족하지 못하는 경우, 구조물을 제거할 수 없기 때문에 복구

```
"""
2:20 시작
2:55 완료
기둥은 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
보: (한쪽 끝이 기둥 위) or (다른 보와 양쪽이 모두 연결)


제약사항 마지막에 전부 확인하기
기둥은 위로 향한다, 보는 오른쪽으로 향한다.

가정
- 바닥에 보 안깔림
- 맵을 벗어나는 보나 기둥 없음
- 구조물을 겹치도록 설치하는 경우 없음
- 없는 구조물을 삭제하는 경우는 없음
"""

TOWER = 0
BEAM = 1
def solution(n, build_frame):
    board = set()
    def contains(y, x, t):
        return (y, x, t) in board
    
    def check_tower(y, x) -> bool:
        # 기둥은 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
        if y == 0:
            return True
        if contains(y-1, x, TOWER): # 아래에 기둥 있으면
            return True
        
        # 아래의 보 하나 이상 있으면
        if contains(y, x-1, BEAM) or contains(y, x, BEAM):
            return True
        return False
    def check_beam(y, x) -> bool:
        # (한쪽 끝이 기둥 위) or (다른 보와 양쪽이 모두 연결)
        
        # 바닥: 방어 코딩
        if y == 0:
            return False
        
        # (한쪽 끝이 기둥 위)
        if contains(y-1, x, TOWER) or contains(y-1, x+1, TOWER):
            return True
        
        # (다른 보와 양쪽이 모두 연결)
        if contains(y, x-1, BEAM) and contains(y, x+1, BEAM):
            return True
        
            
    def add_tower(y, x):
        if check_tower(y,x):
            board.add((y, x, TOWER))
    def add_beam(y, x):
        if check_beam(y,x):
            board.add((y, x, BEAM))
    
    def validate(y, x, a):
        # 문제 없음
        if not contains(y, x, a):
            return True
        # 존재할 경우
        if a == TOWER:
            if check_tower(y, x):
                return True
        else:
            if check_beam(y, x):
                return True
        return False
                
    def remove_tower(y, x) :
        # top을 제거하면 해당 포인트 위에 있는 top 1개에 대해 검사 TODO
        # top을 제거하면, 해당 포인트에 연결된 보가 2개에 대해 검사
        board.remove((y,x,TOWER))
        success = True
        if not validate(y+1, x, TOWER):
            success = False
        
        if not validate(y+1, x-1, BEAM):
            success = False
        if not validate(y+1, x, BEAM):
            success = False
        if not success:
            board.add((y,x,TOWER))
    def remove_beam(y,x):
        board.remove((y, x, BEAM))
        success = True
        
        if not validate(y, x, TOWER):
            success = False
        if not validate(y, x+1, TOWER):
            success = False
        
        if not validate(y, x-1, BEAM):
            success = False
        if not validate(y, x+1, BEAM):
            success = False
        if not success:
            board.add((y,x,BEAM))
        
    for x, y, a, b in build_frame:
        # 추가 모드
        if b:
            if a == 0:
                add_tower(y,x)
            else:
                add_beam(y,x)
        else:
            if a == 0:
                remove_tower(y,x)
            else:
                remove_beam(y,x)
    answer = []
    for y, x, a in board:
        answer.append([x, y, a])
    return sorted(answer)
```