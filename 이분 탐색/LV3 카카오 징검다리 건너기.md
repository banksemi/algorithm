[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/64062
- 문제 접근법과 bigO까지는 맞는데, 시간 초과때문에 효율성 점수를 받지 못했다.
1. 가지치기가 가능한지 확인하자
2. 불필요한 변수 호출이나 갱신이 있는지 확인하자
3. max_i를 직접 선언할 수 있다면 선언하자, 이분탐색의 시간이 2배로 소요된다.

4개의 효율성 개선 방안 추가 코드
```
"""
규칙
- 디딤돌을 밟을때마다 돌 숫자가 1 줄어든다.
- 숫자가 0이 되면 더 이상 밟을 수 없다. (그러면 다음 디딤돌로 한번에 여러 칸 건너 뛸 수 있다)
- 중요: 한번에 돌을 여러개 건너띌 수 없다.

최대 몇명 건널 수 있는가?

stones: 돌 개수: 1~20만, 각 원소 2억 이하
k는 1 이상, stones 이하

결정 문제로 바꿀 수 있나?

최대 몇명까지 징검다리를 건널 수 있나요?
-> n명이 있을 때 징검다리를 건널 수 있나요?
-> n-1명이 일단 돌 다 두드리면서 건너본다. (음수도 있고, 안되는 경우도 있을거다)(근데 여기서 문제를 안잡아도 n명째에서 사고가 난다.)
-> 5명이 건널려면 돌이 k보다 큰게 
"""
import sys
sys.setrecursionlimit(2**30)
def solution(stones, k):
    # stones = [200_000_000] * 200_000
    def check(n): # n명이 있을 때 징검 다리를 건널 수 있는지 본다.
        offset = n-1
        
        need_k = 1
        for i in stones: # TODO 마지막 돌 생각해야함 - 어차피 자동 계산
            # stone_life = i - offset # 효율성 1: 변수 선언 X
                
            if i - offset <= 0: # 효율성 2: stones[i] 대신 i 사용
                need_k += 1
                if need_k > k: # 효율성 3: 가지치기
                    return False
            else:
                need_k = 1
        return True
    
    def bsearch(min_i, max_i):
        if min_i == max_i:
            return min_i - 1 # 불가능해지면 한칸 앞에꺼가 가능한거.
        m = (min_i + max_i) // 2
        
        if check(m): # 가능하면 더 큰 값을 써본다.
            return bsearch(m+1, max_i)
        else:
            return bsearch(min_i, m)
     
    # 효율성 4: max_i를 직접 정의
    #max_i = 2
    #while check(max_i):
    #    max_i *= 2
    return bsearch(0, 200_000_001)
```

---
1차 풀이 (오답)
- nlogm 인데 시간 초과의 이유를 알 수 없다.
```
"""
규칙
- 디딤돌을 밟을때마다 돌 숫자가 1 줄어든다.
- 숫자가 0이 되면 더 이상 밟을 수 없다. (그러면 다음 디딤돌로 한번에 여러 칸 건너 뛸 수 있다)
- 중요: 한번에 돌을 여러개 건너띌 수 없다.

최대 몇명 건널 수 있는가?

stones: 돌 개수: 1~20만, 각 원소 2억 이하
k는 1 이상, stones 이하

결정 문제로 바꿀 수 있나?

최대 몇명까지 징검다리를 건널 수 있나요?
-> n명이 있을 때 징검다리를 건널 수 있나요?
-> n-1명이 일단 돌 다 두드리면서 건너본다. (음수도 있고, 안되는 경우도 있을거다)(근데 여기서 문제를 안잡아도 n명째에서 사고가 난다.)
-> 5명이 건널려면 돌이 k보다 큰게 
"""
import sys
sys.setrecursionlimit(2**30)
def solution(stones, k):
    # stones = [200_000_000] * 200_000
    def check(n): # n명이 있을 때 징검 다리를 건널 수 있는지 본다.
        offset = n-1
        
        need_k = 1
        current = 1
        for i in range(len(stones)): # TODO 마지막 돌 생각해야함 - 어차피 자동 계산
            stone_life = stones[i] - offset
                
            if stone_life <= 0:
                current += 1
                need_k = max(need_k, current)
            else:
                current = 1
        return need_k <= k
    
    def bsearch(min_i, max_i):
        if min_i == max_i:
            return min_i - 1 # 불가능해지면 한칸 앞에꺼가 가능한거.
        m = (min_i + max_i) // 2
        
        if check(m): # 가능하면 더 큰 값을 써본다.
            return bsearch(m+1, max_i)
        else:
            return bsearch(min_i, m)
    
    max_i = 2
    while check(max_i):
        max_i *= 2
    return bsearch(0, max_i)
```