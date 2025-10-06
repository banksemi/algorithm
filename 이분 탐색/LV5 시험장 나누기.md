[나중에 다시 풀어보기] https://school.programmers.co.kr/learn/courses/30/lessons/81305

LV4 징검다리를 공부하고, 유사한 문제 패턴을 인지할 수 있었다. 이전 문제에서 문제 접근법에 힌트를 받았기 때문에, 나중에 다시 풀어봐야할 것 같다.

과정
- 1. 너무 많은 파라미터 조합을 찾기 위한 방법을 결정 문제로 바꾼다.
- 2. 답을 정해두고, 그 답을 허용할 수 있는지 확인한다. (보통 그리디 접근으로 해결되는 경우가 많다)


```
"""
'최소화된 그룹 인원'

쪼갤 횟수 = k (최대 1만번 쪼갤 예정)

결정 문제로 바꿀 수 있는지 고민해보자 -> 결정 문제는 풀기가 더 쉽다!!
check(target) -> 모든 그룹이 target 이하를 유지할 수 있는 경우의 수가 1개 이상 있는가?


"""
import sys

def solution(k, num, links):
    nodes = {}
    find_parent_set = set(range(len(num)))
    for i in range(len(num)):
        nodes[i] = []
    
    for i, value in enumerate(links):
        for j in value:
            if j != -1:
                nodes[i].append(j)
                if j in find_parent_set:
                    find_parent_set.remove(j)
    
    root_node = list(find_parent_set)[0]
    def check(target):
        # 먼저 모든 노드가 target 보다 작거나 같은지 확인한다.
        if max(num) > target:
            return False
        
        use_k = 0
        def dfs(parent): # 현재 그룹 수
            nonlocal use_k
            # 하위 그룹이 없는 경우 자를 수도 없고 그대로 반환해야한다.
            if not nodes[parent]:
                return num[parent]
            
            counts = []
            for child in nodes[parent]:
                counts.append(dfs(child))
            
            total_value = num[parent] + sum(counts)
            if total_value <= target:
                return total_value
            
            # 문제가 있어서 어떻게든 분할을 해야함
            counts = sorted(counts, reverse=True) # 가능한 큰 그룹부터 잘라보는게 이득임. 근데 잘랏는데도 여전히 초과하면 둘다 잘라야함
            for child, child_count in zip(nodes[parent], counts):
                # print(f'자른다 {parent} 아아래 그룹 숫자, {child_count}')
                total_value -= child_count
                use_k += 1
                if total_value <= target:
                    return total_value
            return total_value
        dfs(root_node)
        return k-1 >= use_k
    
    def bsearch(min_i, max_i):
        m = (min_i + max_i) // 2
        if min_i == max_i:
            return min_i
        if check(m): # 가능 하면 조금 줄인다.
            return bsearch(min_i, m)
        else:
            return bsearch(m+1, max_i)
    return bsearch(0, 10000 * 10000 * 10)
```