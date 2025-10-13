https://school.programmers.co.kr/learn/courses/30/lessons/17683

문자열 부분 매치 알고리즘

in (파이썬 내장 구문)을 통해 문자열을 비교하였으나, 직접 반복문을 통해 문자열을 스캔해보고, KMP 알고리즘을 통해서도 접근해볼 예정이다.

```
from string import ascii_letters

def text_search(full_text, search_text):
    return search_text in full_text

def time_str_to_int(text):
    arr = [int(i) for i in text.split(':')]
    return arr[0] * 60 + arr[1]

def parse(song):
    for a, A in zip(ascii_letters, ascii_letters.upper()):
        song = song.replace(f'{A}#', a)
    return song

def solution(m, musicinfos):
    m = parse(m)
    result = []
    for i, line in enumerate(musicinfos):
        start_time, end_time, title, song = line.split(',')
        play_time = time_str_to_int(end_time) - time_str_to_int(start_time)
        song = parse(song)
        song = song * (play_time // len(song) + 1)
        if text_search(song[0:play_time], m):
            # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 
            # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
            result.append([-play_time, i, title])
            
    if result:
        return sorted(result)[0][2] # title
    else:
        return '(None)'
```