https://school.programmers.co.kr/learn/courses/30/lessons/92343

[틀림]

이 문제는 모든 경로를 고려하는 문제이다. 특히 백 트래킹 개념이 결합되어 노드 방문 순서에 따라 결과가 달라질 수 있다.


처음 답(블로그 참고해서 품)
- 방문한 노드를 visited로 관리한다.
- **중요 개념: 해당 노드에서 움직이지 않고 모든 엣지를 보고 이동하지 않았던 엣지로 탐색한다**
- **즉 '현재 노드'에서 움직이는 개념이 아니라 모든 방문 가능한 노드를 탐색한다**

```
"""
양<=늑대 -> 모든 양이 먹힌다.

즉 양이 잡아먹히지 않도록(전제)하면서 최대한 많은 양 

노드 수: 17


노드 방문
- 왼쪽부터 갈까 오른쪽부터 갈까? 두 케이스 모두 고려
- 그리고 가능한 모든 가지수를 만들어 위로 반환.
"""

def solution(info, edges):
    nodes = {}
    
    for i in range(len(info)):
        nodes[i] = []
    
    for n1, n2 in edges:
        nodes[n1].append(n2)
    
    visited = [False] * len(info)
    result = 0
    def dfs(node, n1, n2):
        nonlocal result
        try:
            visited[node] = True
            if info[node] == 0:
                n1 += 1
            else:
                n2 += 1
                if n1 <= n2:
                    return
            result = max(result, n1)
            for s, e in edges:
                if visited[s] == True and visited[e] == False:
                    dfs(e, n1, n2)
        finally:
            visited[node] = False
            
        
    dfs(0, 0, 0)
    return result
```

