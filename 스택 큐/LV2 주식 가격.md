[틀림] https://school.programmers.co.kr/learn/courses/30/lessons/42584
- 스택을 통해 주식 가격을 넣고, 가격이 떨어지면 스택에서 빼준다.
	- 이렇게하면 주식 가격은 항상 오름차순 정렬이 되어있다.
- 틀린 부분: if -> while

```
"""
(0, 1)
(1, 2)
(2, 3)
(3, 2), (2,3 빼기)


"""
def solution(prices):
    result = {}
    stack = []
    for i, price in enumerate(prices):
        key = (i, price)
        while stack and stack[-1][1] > price:
            result[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append(key)
        
    answer = []
    for i in range(len(prices)):
        if i not in result:
            answer.append(len(prices)-i-1)
        else:
            answer.append(result[i])
    return answer
```