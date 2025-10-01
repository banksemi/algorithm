```
"""
직원수 2 이상, 30만 이하 (각각 버는 금액 1만)


팀장을 줄때, 팀원 중 한명을 골랐을 때 최적의 값이 나와야함

무조건 팀장이거나 팀원이거나, 팀장팀장X, 팀원팀원X
- 팀원, 팀장+팀원, 팀장

def max_value(team_number) -> [팀장이갈때, 팀원이갈때]:
    -> 이 팀안에서는 최적의 해를 보장해야한다.
    -> 근데 팀장이 올때, 팀원이 올때가 될 수 있다.
    -> 팀장이 올때는, 그 팀장을 팀원 겸용으로 쓸 수 있다.
    

teams[팀장번호] = [팀원번호1, 팀원번호2]

"""
from functools import lru_cache
def solution(sales, links):
    teams = {}
    for leader, member in links:
        if leader not in teams:
            teams[leader] = []
        teams[leader].append(member)
        
    def get_value(i):
        return sales[i-1]
    
    @lru_cache(maxsize=None)
    def min_value(leader): # -> [팀장으로 갈때 최소화된 손실, 팀원으로 갈때 최소화된 손실]
        # 멤버가 없으면 리더 혼자 희생할 수 밖에 없음
        if leader not in teams:
            return (get_value(leader), 0)
        
        # 팀장이 희생하지 않는 경우 -> 아래 팀원 중 하나 이상은 리더가 포함되어야함
        leader_value = 1e9
        for workshop_member in teams[leader]:
            _value = 0
            for member in teams[leader]:
                if workshop_member == member:
                    _value += min_value(member)[0]
                else:
                    # 아래의 직원은 알아서 자체적으로 해결해야함
                    _value += min(min_value(member))
            leader_value = min(leader_value, _value)
            
        member_value = get_value(leader)
        # 팀장이 희생하는 경우 -> 아래 팀은 자체적으로 해결이 되면 됨.
        for member in teams[leader]:
            _value = min(min_value(member))
            member_value += _value

        return (member_value, leader_value)

    return min(min_value(1))
```