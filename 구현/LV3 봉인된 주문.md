[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/389481
'a' -> 'b' -> 'c'.... 'z' -> 'aa' 이런식으로 문자들이 존재하고 일부 요소가 누락되었을때, 배열의 n번째 위치의 값을 찾는 문제다.

이 문제를 풀기 위해 가장 중요한 것은 문자열 순서를 어떻게 숫자에 매핑하는지 고민하는 것이다.
- 'a'를 '0'으로 매핑하면 'aa'를 표현하기 어렵고, 'a'를 1로 매핑하면 'z' 다음 'aa'가 되었을 때 숫자가 점프되게 된다.

따라서 규칙을 숫자에 0부터 차곡차곡 매핑하는 알고리즘부터 작성했다.
- 'HH:MM:SS'와 같은 string을 int로 변환하는 로직과 비슷하지만 한가지 예외가 추가되었다.
- 앞부분(HH, MM)에 대해서는 각각 값을 +1 한 것으로 가정하고 계산
- 이렇게해야 'aa'가 되었을 때 `(0+1)*26+1` 으로 표현이 가능하다.

반대로 숫자를 영어로 바꾸는 로직은 위의 로직을 역으로 구현했다.
- 26으로 나눠가면서 나머지를 통해 뒷부분을 구한다.
- 앞부분에는 1을 빼고 다시 이 과정을 반복한다.

추가 규칙
- [0,1,2,3,4,5] 에서 3,4가 제거된다고 하자.
- 이때 arr[3]을 구하면 5가 나와야한다.
	- 값이 제거될때마다 한칸씩 땡겨졌기 때문에 '4' index까지 순서 결정에 반영하게 되는 원리
- 이 규칙을 잘못 생각해서 중복 적용하여 오답이 나오게 되었다.


```
"""
12:00 시작
12:42 실패
12:43 skip_numbers = sorted([string_to_int(data) for i, data in enumerate(bans)]) 논리 오류 수정 후 통과

조건
- 각 주문은 알파벳 소문자 11글자 이하

각 주문을 숫자 순서로 바꾼다.
삭제된 숫자들을 정렬한다.
찾고자 하는 n 앞에 삭제된 숫자가 몇개인지 확인한다.

n-삭제된 숫자를 다시 영어로 바꾸고 반환한다.
"""
from string import ascii_lowercase
base = len(ascii_lowercase)
base_char_to_int = {
    value: i for i, value in enumerate(ascii_lowercase)
}
base_int_to_char = {
    i: value for i, value in enumerate(ascii_lowercase)
}
def solution(n, bans):
    def string_to_int(text):
        value = 0
        for i, char in enumerate(text):
            if i > 0:
                value = (value + 1) * base
            value += base_char_to_int[char]
        return value
    
    def int_to_string(value):
        text = ''
        while True:
            d, m = divmod(value, base)
            text = base_int_to_char[m] + text
            value = d
            if value == 0:
                return text
            value -= 1

    skip_numbers = sorted([string_to_int(data) for i, data in enumerate(bans)])
    skipped = 0
    for i in skip_numbers:
        if i-skipped < n:
            skipped += 1
    return int_to_string(n+skipped-1)
```