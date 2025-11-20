---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/118668
문제 유형:
  - DP(Bottom-up)
  - 다익스트라
풀이 날짜: 2025-11-20
정답 여부: 오답
틀린 이유:
  - 최적화
  - 아이디어
  - 임계값 테스트 코드 누락
마지막 풀이 날짜:
---


DP(bottom-up 풀이)
- DP 테이블을 구성하고, 모든 problem을 반복하며 한칸씩 채우는 방식으로 진행해야함.
- 또한 'problem'별로 반복하는 방식은 불가능하다 (처음 생각한 방식)
	- 각 문제마다 요구사항이 있기 때문에 순서에 의존성이 발생한다.
```
MAX_SIZE = 150
def solution(alp, cop, problems):
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    dp = [[999] * (MAX_SIZE+1) for _ in range(MAX_SIZE+1)]

    target_alp = max([i[0] for i in problems])
    target_cop = max([i[1] for i in problems])
    
    # 만약 목표보다 현재 레벨이 높은 경우 (낮은 지점은 업데이트를 생략했기 때문에 불가)
    target_alp = max(alp,target_alp)
    target_cop = max(cop,target_cop)
    
    dp[alp][cop] = 0
    for a in range(alp, target_alp + 1):
        for b in range(cop, target_cop + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a < alp_req or b < cop_req:
                    continue
                # 최적화 포인트
                t_alp = min(a + alp_rwd, target_alp)
                t_cop = min(b + cop_rwd, target_cop)
                
                dp[t_alp][t_cop] = min(dp[t_alp][t_cop], dp[a][b] + cost)
                

    return dp[target_alp][target_cop]
```


다익스트라 풀이
- 상태를 갱신하며 새로운 상태(alp, cop)를 가장 먼저 탐색할 때 발생하는 비용 반환
```
from heapq import heappush, heappop

def solution(alp, cop, problems):
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    target_alp = max([i[0] for i in problems])
    target_cop = max([i[1] for i in problems])
    
    visited = set()
    queue = []
    queue.append((0, alp, cop))
    
    while queue:
        current_cost, alp, cop = heappop(queue)
        if (alp, cop) in visited:
            continue
        visited.add((alp, cop))
        if alp >= target_alp and cop >= target_cop:
            return current_cost
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp < alp_req:
                continue
            if cop < cop_req:
                continue
            new_alp = min(alp+alp_rwd, target_alp)
            new_cop = min(cop+cop_rwd, target_cop)
            if (new_alp, new_cop) in visited:
                continue
                
            heappush(queue, (current_cost+cost, new_alp, new_cop))
```