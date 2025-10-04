https://school.programmers.co.kr/learn/courses/30/lessons/64064


틀림.

힌트 보고도 조금 어렵게 돌아가서 만들었다. 일단 여기서 얻을 수 있는 문제 패턴은,,,
(1,2), (1,2,3), (2,3) 이렇게 3개의 인물이 가질 수 있는 자원 경우의 수가 있을 때, 1개씩 소유할 수 있는지??

-> 다른 방법이 없는지 생각해봐야할 것 같다.

```
from itertools import product, permutations

def check(user, banned):
    if len(user) != len(banned):
        return False
    
    for i, j in zip(user, banned):
        if j == '*':
            continue
        if i != j:
            return False
    return True

    
def function(users, banned_users):
    # 사용자와 벤 사용자가 1:1로 매치되는지 확인하는 함수
    
    if len(users) != len(banned_users):
        return False
    
    # 각 유저별로 가능한 Banned 아이디를 연결
    temp = {
        user: set() for user in users
    }
    for i, banned in enumerate(banned_users):
        for user in users:
            if check(user, banned):
                temp[user].add(i)
                
    # 모든 유저가 한개의 밴 번호와 연결될 수 있는 케이스 찾기
    temp = list(temp.values())
    for ban_case in permutations(range(0, len(temp))):
        failed = False
        for value, target in zip(temp, ban_case):
            if target not in value:
                failed = True
                break
        if not failed:
            return True
    return False
    
def solution(user_id, banned_id):
    answer = 0
    for arr in product([False, True], repeat=len(user_id)):
        new_users = [i for i, j in zip(user_id, arr) if j]
        if function(new_users, banned_id):
            answer += 1
    return answer
```