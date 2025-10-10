https://school.programmers.co.kr/learn/courses/30/lessons/72410

처음 짠 코드에서 s = s.strip('.')  , s.lower()을 사용해서 줄일 수 있다.

```
"""
3:58 시작 -> 4:10 종료

규칙에 맞지 않을 때 -> 규칙에 맞는 아이디 추천.

1. 아이디 3글자 이상, 15자 이하
2. 알파벳 소문자, 숫자, -, _, . 만 사용 가능
3. 마침표 .는 처음과 끝에 사용 못함. 연속도 안됨.

"""
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
available = '-._' + 'abcdefghijklmnopqrstuvwxyz' + '0123456789'

print = lambda *args, **kwargs:...

def check(text):
    length = len(text)
    if length < 3 or length > 15:
        return False
    
    for i in text:
        if i not in available:
            return False
    if text[0] == '.' or text[-1] == '.':
        return False
    return True

def solution(new_id):
    if check(new_id):
        return new_id
    
    # 1단계
    for a, A in zip(abc, ABC):
        new_id = new_id.replace(A, a)
    print("1단계 완료", new_id)
    
    # 2단계
    _temp = ''
    for i in new_id:
        if i in available:
            _temp += i
    new_id = _temp
    print("2단계 완료", new_id)
    
    # 3eksrP
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    print("3단계 완료", new_id)
    # 4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    print("4단계 완료", new_id)
    # 5 단계
    if not new_id:
        new_id = 'a'
    
    # 6 단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
```