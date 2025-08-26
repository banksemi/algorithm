https://school.programmers.co.kr/learn/courses/30/lessons/42842

문제의 중요한건 브라운이 한줄이라는 것.

그림으로 그려보니까 브라운 개수는 x랑 y를 통해 수식으로 정리된다.

x+y = (브라운 + 4) / 2


그러면 x+y 값을 구하고 x 1 증가, y 1 감소 방식으로 하나씩 바꿔가면서 노란색 크기가 주어진 크기랑 일치하는지만 보면 해결이 된다.

```
def solution(brown, yellow):
    x_plus_y = int((brown + 4) / 2)
    
    for x in range(0, x_plus_y):
        y = x_plus_y - x
        
        if (x-2) * (y-2) == yellow:
            if x > y:
                return [x, y]
            else:
                return [y,x]
    answer = []
    return answer
```