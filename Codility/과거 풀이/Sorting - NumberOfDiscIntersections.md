[틀림]

시간 복잡도와 -1 처리에서 오류가 발생했다.
- 아래에 문제 조건을 꼼꼼하게 읽자.
- 그리고 스위핑 라인 알고리즘을 기억하자.

스위핑 라인 알고리즘
- 겹치는 구간을 산정하거나 개수를 셀 때 유용하다.

다음처럼 이벤트로 만든다.
- 1, start
- 3, end
- 2, start
- 4, end

정렬한다. 이때 start, end중 무엇을 우선적으로 해야할지는 문제에 따라 잘 정의해야한다.
- 반닫힘 구간일때 - end 우선
- 점으로 만나는 지점도 겹치는 구간으로 볼 때 - start 우선 

```
# 디스크 N개가 있음.
# 디스크들은 0에서 N-1까지임.
# 양수(0포함) N으로 이루어진 A 배열
# 그 디스크의 센터는 J이고 반지름은 A[J]
"""
  A[0] = 1  (-1, 0, 1)
  A[1] = 5  (-4,1,6)
  A[2] = 2  (0,2,4)
  A[3] = 1  (2,3,4)
  A[4] = 4  (0,4,8)
  A[5] = 0  (5,5,5)
"""
START = 0
END = 1
def solution(A):
    events = []
    for i, r in enumerate(A):
        events.append((
            i-r, START
        ))
        events.append((
            i+r, END
        ))
    events.sort()
    opened = 0
    result = 0
    for event in events:
        # print(event, "open" if event[1] == START else 'close')
        if event[1] == START:
            result += opened # 열려있는 만큼 중복되었다.
            if result > 10_000_000:
                return -1
            opened += 1
        else: # 닫히는거면
            opened -= 1
    return result
```