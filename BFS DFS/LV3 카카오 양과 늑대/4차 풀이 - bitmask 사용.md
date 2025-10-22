https://school.programmers.co.kr/learn/courses/30/lessons/92343

방문 가능한 노드를 bitmask로 표현하여 문제를 다시 풀어봤다.
- 특정 비트를 OFF 시키는 방법은 XOR을 사용하거나 OR(+NOT)을 사용할 수 있다.
	- bitmask ^= 1 << node # 혹은 bitmask &= ~(1<<node)
	- 물론 XOR을 사용하기 전 해당 비트가 ON이라는 가정이 있어야한다.


```
"""
0 양
1 늑대

"""

from collections import defaultdict
def solution(info, edges):
    nodes = defaultdict(list)
    for a, b in edges:
        nodes[a].append(b)
    
    def dfs(node, bitmask, a, b):
        if info[node] == 0:
            a += 1
        else:
            b += 1
            if a <= b:
                return -1
        # 이번 꺼 방문 처리
        bitmask ^= 1 << node # 혹은 bitmask &= ~(1<<node)
        for child in nodes[node]:
            bitmask |= 1 << child
        
        result = a
        for i in range(len(info)):
            if bitmask & (1 << i):
                result = max(result, dfs(i, bitmask, a, b))
        return result
        
    answer = 0
    return dfs(0, 1, 0, 0)
```

```
정확성  테스트

|   |   |
|---|---|
|테스트 1 〉|통과 (0.01ms, 9.07MB)|
|테스트 2 〉|통과 (0.21ms, 9.3MB)|
|테스트 3 〉|통과 (0.02ms, 9.2MB)|
|테스트 4 〉|통과 (0.01ms, 9.15MB)|
|테스트 5 〉|통과 (0.59ms, 9.1MB)|
|테스트 6 〉|통과 (0.32ms, 9.14MB)|
|테스트 7 〉|통과 (0.17ms, 9.24MB)|
|테스트 8 〉|통과 (0.07ms, 9.23MB)|
|테스트 9 〉|통과 (0.65ms, 9.13MB)|
|테스트 10 〉|통과 (8.00ms, 9.14MB)|
|테스트 11 〉|통과 (0.35ms, 9.14MB)|
|테스트 12 〉|통과 (1.60ms, 9.13MB)|
|테스트 13 〉|통과 (0.05ms, 9.3MB)|
|테스트 14 〉|통과 (0.10ms, 9.14MB)|
|테스트 15 〉|통과 (1.17ms, 9.16MB)|
|테스트 16 〉|통과 (1.13ms, 9.06MB)|
|테스트 17 〉|통과 (18.30ms, 9.1MB)|
|테스트 18 〉|통과 (0.56ms, 9.09MB)|
```