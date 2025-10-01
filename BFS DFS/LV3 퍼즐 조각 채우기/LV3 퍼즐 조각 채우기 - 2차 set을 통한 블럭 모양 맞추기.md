
핵심 로직
- 빈 공간이라는 것도 퍼즐 추출하듯 분리하기.
- 그리고 퍼즐 hash를 만들어서, 동일한 hash 비교하기!

```
def set_hash(puz):
    return str(sorted(puz))
    
for puz in puzs:
	c = set()
	current_puz = puz
	for i in range(4):
		c.add(set_hash(current_puz))
		current_puz = rotate_90(current_puz)
	inter = set(areas) & c
	if inter:
		value += len(puz)
		areas.remove(inter.pop())
```



```
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
from collections import deque

def trim_puz(puz):
    # 0,0에서 시작하게 만들어주기
    min_y = min([i[0] for i in puz])
    min_x = min([i[1] for i in puz])
    return set([(i[0] - min_y, i[1] - min_x) for i in puz])

def set_hash(puz):
    return str(sorted(puz))

def rotate_90(puz):
    # 0, 1, 2
    # 3, 4, 5
    # 6, 7, 8
    # 9, 10, 11
    
    # 9, 6, 3, 0
    # 10, 7, 4, 1
    # 11, 8, 5, 2
    
    # (4,1) -> (1, 0)
    
    # (0,0) -> (x) (height - y - 1)
    
    height = max([i[0] for i in puz]) # 이거 사실 필요없음 trim_puz 덕분에 잘 돌아감
    return trim_puz([(x, -y - 1) for y, x in puz])
    
def solution(game_board, table):
    height = len(game_board)
    width = len(game_board[0])
    
    def split_puz(board, y, x, target_bit):
        queue = deque([(y,x)])
        result = []
        while queue:
            item = queue.popleft()
            y = item[0]
            x = item[1]
            if board[y][x] != target_bit:
                continue
            board[y][x] = 999
            
            result.append(item)
            for dir in dirs:
                y = item[0] + dir[0]
                x = item[1] + dir[1]
                if x < 0 or y < 0:
                    continue
                if x >= width or y >= height:
                    continue
                if board[y][x] != target_bit:
                    continue
                queue.append((y, x))
        return trim_puz(result)
    
    # 퍼즐 분리하기
    puzs = []
    areas = []
    for y in range(height):
        for x in range(width):
            if table[y][x] == 1:
                puzs.append(split_puz(table, y, x, target_bit=1))
            
            if game_board[y][x] == 0:
                area = split_puz(game_board, y, x, target_bit=0)
                areas.append(set_hash(area))
    
    value = 0
    for puz in puzs:
        c = set()
        current_puz = puz
        for i in range(4):
            c.add(set_hash(current_puz))
            current_puz = rotate_90(current_puz)
        inter = set(areas) & c
        if inter:
            value += len(puz)
            areas.remove(inter.pop())
        
    return value
```