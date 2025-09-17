https://school.programmers.co.kr/learn/courses/30/lessons/42892

[1차 재귀 함수 런타임 에러] `sys.setrecursionlimit(1_000_000_000)` 잊지 말자!
[후위 탐색] 내가 후위 탐색이 기억나지 않아 복잡한 알고리즘으로 풀었다.
- 내 알고리즘: 리프노드 찾은 후 바텀 업 방식으로 부모 노드 접근, 부모 노드의 차수가 1 이상 남아있으면 다음 리프노드로 이동.
- 원래 방식: DFS 로 탐색하는데 부모 노드를 마지막에 등록.


```
import sys
sys.setrecursionlimit(1_000_000_000)
def solution(nodeinfo): # [x축 좌표, y축 좌표] i+1번 노드
    temp = []
    for i, xy in enumerate(nodeinfo):
        temp.append((i+1, xy[0], xy[1]))

    nodes = {}
    for i in range(1, len(nodeinfo) + 1):
        nodes[i] = []
    
    def make_nodes(parent, temp):
        # parent 기준으로 좌 우 나누기
        left_temp = []
        right_temp = []
        left_head = None
        right_head = None
        
        for ixy in temp:
            if ixy[1] < parent[1]:
                left_temp.append(ixy)
                if left_head is None or left_head[2] < ixy[2]:
                    left_head = ixy
            elif ixy[1] > parent[1]:
                right_temp.append(ixy)
                if right_head is None or right_head[2] < ixy[2]:
                    right_head = ixy

        if left_head:
            nodes[parent[0]].append(left_head[0])
            make_nodes(left_head, left_temp)
            
        if right_head:
            nodes[parent[0]].append(right_head[0])
            make_nodes(right_head, right_temp)

    head_node = sorted(temp, key=lambda node: -node[2])[0]
    head_node_i = head_node[0]
    make_nodes(head_node, sorted(temp, key=lambda node: node[1]))
    
    preorder_result = []
    postorder_result = []
    
    def preorder(node):
        preorder_result.append(node)
        for i in nodes[node]:
            preorder(i)
    
    def postorder(node):
        for i in nodes[node]:
            postorder(i)
        postorder_result.append(node)
        
    preorder(head_node_i)
    postorder(head_node_i)
    return [preorder_result, postorder_result]
```


--- 과거 코드 ---

```
import sys
sys.setrecursionlimit(1_000_000_000)
def solution(nodeinfo): # [x축 좌표, y축 좌표] i+1번 노드
    temp = []
    node_to_xy = {}
    for i, xy in enumerate(nodeinfo):
        temp.append((i+1, xy[0], xy[1]))
        node_to_xy[i+1] = (xy[0], xy[1])

    nodes = {}
    parents = {}
    for i in range(1, len(nodeinfo) + 1):
        nodes[i] = []
    
    def make_nodes(parent, temp):
        # parent 기준으로 좌 우 나누기
        left_temp = []
        right_temp = []
        left_head = None
        right_head = None
        
        for ixy in temp:
            if ixy[1] < parent[1]:
                left_temp.append(ixy)
                if left_head is None or left_head[2] < ixy[2]:
                    left_head = ixy
            elif ixy[1] > parent[1]:
                right_temp.append(ixy)
                if right_head is None or right_head[2] < ixy[2]:
                    right_head = ixy

        if left_head:
            nodes[parent[0]].append(left_head[0])
            parents[left_head[0]] = parent[0]
            make_nodes(left_head, left_temp)
            
        if right_head:
            nodes[parent[0]].append(right_head[0])
            parents[right_head[0]] = parent[0]
            make_nodes(right_head, right_temp)

    head_node = sorted(temp, key=lambda node: -node[2])[0]
    head_node_i = head_node[0]
    make_nodes(head_node, sorted(temp, key=lambda node: node[1]))
    
    preorder_result = []
    postorder_result = []
    
    def preorder(node):
        preorder_result.append(node)
        for i in nodes[node]:
            preorder(i)
    
    preorder(head_node_i)
    leaf_nodes = []
    for i, childs in nodes.items():
        if not childs:
            leaf_nodes.append(i)
    
    leaf_nodes.sort(key=lambda i: node_to_xy[i][0])
    
    for leaf in leaf_nodes:
        current = leaf
        while True:
            postorder_result.append(current)
            parent = parents[current] if current in parents else None
            
            if parent is not None:
                nodes[parent].remove(current)
            
            if parent is not None and len(nodes[parent]) == 0:
                current = parent
            else:
                break

    return [preorder_result, postorder_result]
```