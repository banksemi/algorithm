https://school.programmers.co.kr/learn/courses/30/lessons/42884

그리디 문제, 특별한 이슈 없음.

```
"""
문제: 모든 차량이 한번은 단속 카메라를 만나게 하려면 최소 몇개

차량 수: 1만대 이하 (최소 1)

routes[i] = [진입 시점, 나간 시점] <- 끝 부분도 만났다고 치자.

고속도로는 -3만 ~ +3만

시작 지점, 끝 지점을 이벤트로 만들어서 끝 지점을 지나갈 때 카운트를 하나 넣자.
끝 지점에다가 최대한 설치해보자. (최선)

수정
- 'start' 도 사용해서 이전 카메라가 새로운 범위를 커버하는지 보자.
"""
def solution(routes):
    events = []
    for s, e in routes:
        events.append((e, s)) # 끝
    
    events.sort()
    answer = 0
    last_camera = -1e9
    for end, start in events:
        # 카메라가 설치 안되있었다면
        if start > last_camera:
            answer += 1
            last_camera = end
        
    return answer
```