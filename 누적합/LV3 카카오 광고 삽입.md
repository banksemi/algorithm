https://school.programmers.co.kr/learn/courses/30/lessons/72414

이벤트(START, END) 시뮬레이션에 누적합을 적용하는 문제.
- 길이가 정해진 구간을 사용하여 최대 누적합 구간을 찾아야한다.
- 다만 구간이 정해져있다는 특징을 사용하여, 단순히 슬라이딩 윈도우로 풀었다.

처음에는 단순히 '많은 시청자가 1초 이상 볼 수 있는' 지점을 찾으려고 코드를 짰다가, 문제를 다시 읽고 재구현했다. 이 과정에서 불필요한 시간이 많이 소요되었다.

```
"""
시작 10:26 -> 11:18 종료

가장 많이 보는 구간에 공익 광고, 공익 광고의 재생 시간을 준다.
- 그 중 가장 빠른 시작 시간
logs = 300,000

events  = (start or end, 시각)
각 주요 타이밍(들어오고 나간 시간에 따라서)
- 해당 시각의 시청자 수를 테이블에 구해둔다.

그리고 해당 이벤트를 n으로 쭉 스캔하면서
- x분짜리 광고를 실행할때 몇개까지 커버가 되는지를 봐야한다.
- 근데 n을 스캔하면서 앞에를 쭉 보도록하면 n*n으로 시간초과 가능성이 있다.
- 최대한 효율적으로


가정: 끝 부분은 이미 빠져나갔다고함 
"""
def time_to_int(text):
    arr = [int(i) for i in text.split(':')]
    return arr[0] * 3600 + arr[1] * 60 + arr[2]
def int_to_str(value):
    h = value // 3600
    m = (value % 3600) // 60
    s = value % 60
    return f'{h:02}:{m:02}:{s:02}'
END = 0 # END 우선 처리
START = 1
def solution(play_time, adv_time, logs):
    adv_time = time_to_int(adv_time)
    events = []
    for log in logs:
        arr = [time_to_int(i) for i in log.split('-')]
        events.append((START, arr[0]))
        events.append((END, arr[1]))
    events.sort(key=lambda x: (x[1], x[0]))
    
    adv_candidate = {}
    current = 0
    
    for event_type, time in events:
        if event_type == START:
            current += 1
        else:
            current -= 1
        adv_candidate[time] = current
    
    views = [0] * (60 * 60 * 100 + 1)
    _temp = 0
    for i in range(len(views)):
        if i in adv_candidate:
            _temp = adv_candidate[i]
        views[i] = _temp
        
    current = sum(views[0:adv_time])
    max_value = current
    max_value_i = 0
    for i in range(adv_time, len(views)):
        current -= views[i - adv_time]
        current += views[i]
        if max_value < current:
            max_value = current
            max_value_i = i - adv_time + 1
    
    return int_to_str(max_value_i)
```