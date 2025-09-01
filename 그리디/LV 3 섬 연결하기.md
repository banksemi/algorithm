크루스칼 알고리즘 문제.
[틀림] - 틀린 이유는 유니온 함수를 호출할 때 합치는 로직을 잘못 구현했기 때문
- a, b 두 그룹을 합칠때에는, 루트 노드를 찾아서 '루트 노드'가 다른 루트 노드를 보게 합쳐야한다. a, b를 직접 수정하지 말자. (물론 a나 b가 루트노드라면 괜찮지만)

유니온, 파인드를 잘 기억하자.
속도 개선 로직을 기억하자.


```
print = lambda *args, **kwargs:...
def solution(n, costs):
    parents = [i for i in range(n)]
    
    costs = sorted(costs, key=lambda x: x[2])
    def find_parent(a):
        if a == parents[a]:
            return a
        else:
            parents[a] = find_parent(parents[a]) # 속도 개선
            return parents[a]
    
    def union(a, b):
        x1 = find_parent(a)
        x2 = find_parent(b)
        
        if x1 > x2:
            parents[a] = x2
        else:
            parents[b] = x1
    
    result = 0
    for a, b, cost in costs:
        print("확인중", a, b, f"비용{cost}")
        x1 = find_parent(a)
        x2 = find_parent(b)
        print("a", a)
        print("a 부모", x1)
        print("b", b)
        print("b 부모", x2)
        if x1 != x2:
            print("합칠 예정", a, b)
            print("합치는 비용", cost)
            union(x1, x2)
            result += cost
            
    return result
```