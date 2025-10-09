

틀림 - 틀린 이유 - 오타 len(gem) len(gems)

풀이 1
- gem을 하나 더하고, while을 통해 뺄수 있는 만큼**만** left 아이템을 뺀다.
```
"""
모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간

보석 카운트를 한다.
- 부족하면 오른쪽으로 간다.
- 만약 넘치면 가장 왼쪽껄 뺄 수 있는지 본다.
- 조건을 만족하면 정답란에 기록한다([길이, 시작, 끝])
- 나중에 정답란을 정렬하고 가장 작은거 하나를 고르면 된다.
"""
def solution(gems):
    invens = {}
    
    need_gems = set(gems)
    for gem in need_gems:
        invens[gem] = 0
    
    l = 0
    answers = []
    for r, gem in enumerate(gems):
        invens[gem] += 1

        # 없다가 생겼으면 
        if invens[gem] == 1:
            need_gems.remove(gem)

        while l < len(gems) and l < r:
            lose_gem = gems[l]
            if invens[lose_gem] > 1:
                invens[lose_gem] -= 1
            else:
                break
            l += 1

        if not need_gems:
            answers.append([r - l, l+1, r+1])
    return sorted(answers)[0][1:]
```

풀이 2 - while 내에서 두개의 포인터를 함께 관리한다. 
```
def solution(gems):
    n = len(gems)
    invens = {}
    
    need_gems = set(gems)
    for gem in need_gems:
        invens[gem] = 0
    
    l = 0
    r = 0
    answers = []
    while True:
        if need_gems:
            if r == n:
                break
            gem = gems[r]
            if invens[gem] == 0:
                need_gems.remove(gem)
            invens[gem] += 1
            r += 1
            
            # 각각 조건 확인 필요
            if not need_gems:
                answers.append([r-l, l + 1, r])
        if not need_gems:
            if l == n:
                break
            gem = gems[l]
            if invens[gem] == 1:
                need_gems.add(gem)
            invens[gem] -= 1
            l += 1
            # 각각 조건 확인 필요
            if not need_gems:
                answers.append([r-l, l + 1, r])
    return sorted(answers)[0][1:]
```