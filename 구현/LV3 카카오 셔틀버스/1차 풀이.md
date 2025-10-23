[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/17678

구현 및 시뮬레이션 문제. 

두개의 While보다는 한개의 반복문에서 풀었다
- 특히 2개의 배열을 사용하기 때문에 끝 조건을 먼저 정의하고 접근했다.


정답
```
"""
09:00 부터 n회 t분 간격, 최대 m명 탈 수 있음
도착했을 때, 대기열에 있는 만큼만 태우고 바로 출발. (같은 시간에 도착한 사람까지는 가능)

크루 대기열 가장 끝에 선다.
가장 늦게 셔틀 탈 수 있는 시각 구하기

# 모든 사람들마다 뒤에 서서 버스를 타고 갈 수 잇는지 확인

"""
from collections import deque
def time_to_int(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)

def int_to_time(time_int):
    h = time_int // 60
    m = time_int % 60
    return f"{h:02}:{m:02}"

def solution(n, t, m, timetable):
    bus_list = deque()
    _current = time_to_int("09:00")
    for i in range(n):
        bus_list.append([_current + i * t, m])
        
    crews = {}
    for i in timetable:
        _time = time_to_int(i)
        if _time not in crews:
            crews[_time] = 0
        crews[_time] += 1
    crews = deque(sorted([[_time, _count] for _time, _count in crews.items()]))
    
    answer = crews[0][0] - 1
    
    # 투포인터 전략으로 시작
    while True:
        # 더 이상 탈 수 있는 버스가 없는 경우
        if not bus_list:
            break
        
        # 크루가 없지만 버스는 있는 경우
        if not crews:
            # 가장 마지막 버스를 타고 갈 수 있다.
            answer = bus_list[-1][0]
            break
        
        current_bus = bus_list[0]
        crew = crews[0]
        
        # 크루가 버스보다 늦으면, 일단 이 버스는 시간에 맞춰탈 수 있다.
        if crew[0] > current_bus[0]:
            answer = current_bus[0]
            bus_list.popleft()
            continue
        
        # 일단 이 크루는 버스에 탈 수 있기 때문에, 이 사람들보다는 조금 더 일찍 오면 무조건 탈 수 있다.
        answer = max(answer, crew[0]-1)
        available = min(current_bus[1], crew[1])
        crew[1] -= available
        current_bus[1] -= available
        
        if crew[1] == 0:
            crews.popleft()
        
        if current_bus[1] == 0:
            bus_list.popleft()
                
    
    return int_to_time(answer)
```


틀린 버전
```
from collections import deque
def time_to_int(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)

def int_to_time(time_int):
    h = time_int // 60
    m = time_int % 60
    return f"{h:02}:{m:02}"

print = lambda *args, **kwargs:...
def solution(n, t, m, timetable):
    bus_times = deque()
    _current = time_to_int("09:00")
    for i in range(n):
        bus_times.append(_current + i * t)
        
    crews = {}
    for i in timetable:
        _time = time_to_int(i)
        if _time not in crews:
            crews[_time] = 0
        crews[_time] += 1
    crews = deque(sorted([[_time, _count] for _time, _count in crews.items()]))
    
    answer = crews[0][0] - 1
    while bus_times:
        bus_time = bus_times.popleft()
        available = m
        if not crews:
            answer = bus_time
        print("버스 시간", bus_time, m)
        print(list(crews))
        while crews:
            first_crews = crews[0]
            # 만약 첫번째 크루가 못타는 경우, 콘은 그냥 버스 시간에 맞춰서 타고 갈수는 있다.
            if first_crews[0] > bus_time:
                answer = bus_time
                break
            
            # 모든 크루가 탈 수 있으면 타고, 다음 크루로 넘어간다.
            if available >= first_crews[1]:
                available -= first_crews[1]
                crews.popleft()
                
                # 크루 다 타고 자리 있으면 같이 탈 수 있다.
                if available > 0:
                    answer = bus_time
                    # 근데 다음 크루가 늦게 온다면, 그 직전(1분)까지 있을 수 있다.
                    if crews:
                        answer = crews[0][0] - 1
                continue
            
            first_crews[1] -= available # 일단 탈수 있는 만큼만 탄다.
            break # 새로운 버스를 받아야한다.
        
        if not crews and available > 0:
            answer = bus_time
        print(list(crews))
    return int_to_time(answer)
```