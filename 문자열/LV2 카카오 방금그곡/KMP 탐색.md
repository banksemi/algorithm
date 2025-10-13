https://school.programmers.co.kr/learn/courses/30/lessons/17683

KMP 알고리즘을 통해서 문자열 탐색을 진행했다.

KMP 알고리즘이 아직 헷갈리는 부분들이 있어, 나중에 꼭 다시 풀어봐야할 것 같다.


```
from string import ascii_letters

def make_pattern(text):
    arr = [0] * len(text) # n글자 일치
    
    j = 0
    for i in range(1, len(text)):
        while j > 0 and text[i] != text[j]:
            # 이전 j 캐싱 지점으로 돌아간다.
            j = arr[j-1]
        
        if text[i] == text[j]:
            j += 1
            arr[i] = j
    return arr

def text_search(full_text, keyword):
    arr = make_pattern(keyword)
    
    j = 0
    for i in range(0, len(full_text)):
        while j > 0 and full_text[i] != keyword[j]:
            j = arr[j-1]
        
        if full_text[i] == keyword[j]:
            j += 1
        
        if j == len(keyword):
            return True
    
    return False


def time_str_to_int(text):
    arr = [int(i) for i in text.split(':')]
    return arr[0] * 60 + arr[1]

def parse(song):
    for a, A in zip(ascii_letters, ascii_letters.upper()):
        song = song.replace(f'{A}#', a)
    return song

def solution(m, musicinfos):
    print(make_pattern("abcabcdabcd"))
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