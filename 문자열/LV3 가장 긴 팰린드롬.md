[틀림] 짝수로 된 문자열('abba')이 있을 수 있음, 또한 DP로도 문제를 풀 수 있는지 확인 필요

```
"""
문자열길이: 1 ~ 2500
가정: 소문자
"""
def solution(s):
    answer = 1
    
    for m in range(0, len(s)):
        offset=1
        while m-offset >= 0 and m+offset < len(s):
            if s[m-offset] == s[m+offset]:
                answer = max(answer, 1 + offset * 2)
            else:
                break
            offset += 1
            
    for m in range(0, len(s)):
        offset=1
        while m-offset+1 >= 0 and m+offset < len(s):
            if s[m-offset+1] == s[m+offset]:
                answer = max(answer, offset * 2)
            else:
                break
            offset += 1

    return answer
```