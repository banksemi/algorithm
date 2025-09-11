단순한 구현 문제
- Set 자료구조 말고는 특별한 점이 없다.


```
"""
1번부터 순서대로 반복

앞사람이 말한 단어의 마지막 문자로 끝말잇기
- 이미 사용한 단어는 사용 불가
- 한글자 불가

사람 수 n과 words(순서가 있음)가 있을 때 가장 먼저 탈락하는 사람 번호와, 자신의 몇번째 탈락인지

n: 2이상, 50이하
알파벳 소문자
words: 100 이하
** 탈락자가 없으면 0,0을 반환

**단순 시뮬레이션 문제로 접근해보자**
enumera
"""
def solution(n, words):
    answer = []
    known_words = set()
    failed = False
    
    for i, word in enumerate(words):
        if word in known_words:
            failed = True
            break
        
        known_words.add(word)
        
        if len(word) <= 1:
            failed = True
            break

        if i != 0 and word[0] != words[i-1][-1]:
            failed = True
            break
            
    if failed:
        current_round = i // n  + 1
        person = (i % n) + 1
        return [person, current_round]
    return [0, 0]
```