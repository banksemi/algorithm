https://school.programmers.co.kr/learn/courses/30/lessons/72411

문제랑 예외 케이스를 꼭 이해하고 시작하기.
- 급한 마음에 코드부터 짜면 복잡한 코드가 나오게 된다.
2차
```
"""
단품 -> 재구성으로 코스요리

코스요리 조건
- 2가지 이상의 단품 요리 포함
- 최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합

orders: 단품 조합들
course: 허용할 코스 요리 메뉴 수 (2,3,5) -> 2개, 3개, 5개로 구성된 메뉴 들 반환
"""
from itertools import combinations
def solution(orders, course):
    result = {i: {} for i in course}
    
    for order in orders:
        for i in course:
            for arr in combinations(order, i):
                key = ''.join(sorted(arr))
                if key not in result[i]:
                    result[i][key] = 0
                result[i][key] += 1

    answer = []
    
    for i in course:
        if result[i]:
            max_value = max(result[i].values())
            if max_value < 2:
                continue
            answer.extend([key for key, value in result[i].items() if value == max_value])

    return sorted(answer)
```


1차
```
"""
4:20 시작 4:35 종료
단품 -> 재구성으로 코스요리

코스요리 조건
- 2가지 이상의 단품 요리 포함
- 최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합

orders: 단품 조합들
course: 허용할 코스 요리 메뉴 수 (2,3,5) -> 2개, 3개, 5개로 구성된 메뉴 들 반환
"""
from itertools import combinations
def solution(orders, course):
    
    result = {} # dict['AC'] = 1...
    
    for order in orders:
        for i in course:
            for arr in combinations(order, i):
                key = ''.join(sorted(arr))
                if key not in result:
                    result[key] = 0
                result[key] += 1
    
    answer = []
    for key, value in result.items():
        answer.append((key, value))
    
    answer.sort(key=lambda i: (-i[1], i[0]))
    
    added_count = set()
    added_count_value = {}
    result = []
    for key, value in answer:
        if value < 2:
            continue
        if len(key) not in added_count:
            added_count.add(len(key))
            added_count_value[len(key)] = value
            result.append(key)
        else:
            if added_count_value[len(key)] == value:
                result.append(key)
    return sorted(result)
```