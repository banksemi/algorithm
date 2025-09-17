[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/86053

틀린 이유
- [어려웠던 check 함수] 각 도시의 금과 은, 운반 가능 무게가 있을 때 모든 도시의 합을 모아 특정 금, 은을 달성할 수 있는가?
	- 이걸 복잡하게 그리디로 접근했는데 쉬운 풀이가 있었다.
	- 모든 도시의 금 합 >= 목표 금
	- 모든 도시의 은 합 >= 목표 은
	- 모든 도시의 운반량 합 >= 목표 운반량
	- 이 3가지를 만족하면 운반량을 어떻게든 조절할 수 있다?
- [이분 탐색의 최대값] 최대 값 + 1 은 좋았다. 근데 이번 문제는 최대값이 매우 커지는 이슈가 있다. (수십억 이상)
	- [힌트] 최대 값도 ** 2 방식으로 늘려가면서 처음에 구할 수 있었다.
```
    max_i = 1
    while True:
        if check(max_i):
            max_i += 1
            break
        max_i *= 2
```


최종 풀이
```

def solution(a, b, g, s, w, t):
    def check(max_time):
        total_a = 0
        total_b = 0
        total_weight = 0
        
        for i in range(len(w)):
            max_move = (max_time // t[i] + 1) // 2
            max_weight = max_move * w[i] # 최대 운반 가능양
            max_weight = min(g[i] + s[i], max_weight) # 주의: 도시가 가진 만큼만 옮길 수 있다
            total_a += min(g[i], max_weight) # 주의: 옮길 수 있는 만큼만, 가진 것과 동일하다
            total_b += min(s[i], max_weight)
            total_weight += max_weight
        
        if total_a < a:
            return False
        
        if total_b < b:
            return False
        
        if total_weight < a+b:
            return False
        
        return True
    
    def find(min_i, max_i):
        if min_i == max_i:
            return min_i
        m = (min_i + max_i) // 2
        if check(m): # 가능하면 시간을 더 줄여본다.
            return find(min_i, m)
        else: # 불가능하면 시간을 늘린다.
            return find(m+1, max_i)
    
    max_i = 1
    while True:
        if check(max_i):
            max_i += 1
            break
        max_i *= 2
    
    answer = find(0, max_i)
    return answer
```

--- 아래는 첫번째 시도 ---

```
"""
새 도시 건설 장소: a금, b은 만큼 필요함. 1_000_000_000

i 번 도시 100_000
- 금: g[i]
- 은 s[i]
- 트럭: 새 도시 건설 장소로 왕복 가능
- 편도 이동 시간: t[i] 100_000
- 적재량: w[i] (금과 은을 함께 실을 수 있음) 100



단순 문제 변환 - n분 안에 원하는 조건을 달성할 수 있는가?
i 번 도시 100_000
- 금: g[i]
- 은 s[i]
- 트럭: 새 도시 건설 장소로 왕복 가능
- 편도 이동 시간: t[i] 100_000
- 적재량: w[i] (금과 은을 함께 실을 수 있음) 100

더 쉬운 문제 변환 - 각 도시의 광물 최대 값이 있을 때 A 100G, B 90G을 달성할 수 있는가?
각 도시에서 운반 가능한 광물의 양 (도시 10만개)
- A 도시: 150 (은 최대 100) 은 150 보장
- B 도시: 100 (금 최대 100, 은 최대 80) 금 20 보장, 금 or 은 80 가능
"""

print = lambda *args, **kwargs: ...
import copy

def solution(a, b, g, s, w, t):
    def check(max_time):
        print("시간", max_time)
        need_g = a
        need_s = b
        # 각 도시의 [보장금, 보장은, 가변 광물양, 가변금, 가변은]
        temp = []
        for i in range(len(w)):
            max_move = (max_time // t[i] + 1) // 2
            max_weight = max_move * w[i] # 최대 운반 가능양
            
            available_g = g[i]
            available_s = s[i]
            # 모든 짐을 충분히 운반할 수 있는 경우
            if (g[i] + s[i]) < max_weight:
                need_g -= g[i]
                need_s -= s[i]
                available_g = 0
                available_s = 0
                max_weight = 0
            else:
                # 금이 적은 경우, 남은 공간은 실버로 채울수밖에 없음
                if available_g < max_weight:
                    move_s = min(available_s, max_weight - available_g)
                    need_s -= move_s
                    max_weight -= move_s
                    available_s -= move_s
                # 은이 적은 경우 남은 공간을 금으로 채울 수 있음
                if available_s < max_weight:
                    move_g = min(available_g, max_weight - available_s)
                        
                    need_g -= move_g
                    max_weight -= move_g
                    available_g -= move_g
            temp.append([max_weight, min(available_g, max_weight), min(available_s, max_weight)])
        print("해결해야할 금 은", need_g, need_s)
        print("상태", temp)
        if need_g > 0:
            # 금부터 해결하자
            # 금이 많은 곳
            temp.sort(key=lambda x: -x[1])
            for i in range(0, len(temp)):
                if need_g <= 0:
                    break
                move = min(temp[i][1], need_g)
                need_g -= move
                temp[i][0] -= move
                temp[i][1] -= move
                temp[i][2] = min(temp[i][0], temp[i][2])
            if need_g > 0:
                print("금 만족 불가", need_g, temp)
                return False
        if need_s > 0:
            temp.sort(key=lambda x: -x[2])
            for i in range(0, len(temp)):
                if need_s <= 0:
                    break
                move = min(temp[i][2], need_s)
                need_s -= move
                temp[i][0] -= move
                temp[i][1] = min(temp[i][0], temp[i][1])
                temp[i][2] -= move
            if need_s > 0:
                return False
        return True
    
    def find(min_i, max_i):
        if min_i == max_i:
            return min_i
        m = (min_i + max_i) // 2
        if check(m): # 가능하면 시간을 더 줄여본다.
            return find(min_i, m)
        else: # 불가능하면 시간을 늘린다.
            return find(m+1, max_i)
    
    max_i = 1
    while True:
        if check(max_i):
            max_i += 1
            break
        max_i *= 2
    
    answer = find(0, max_i)
    return answer
```