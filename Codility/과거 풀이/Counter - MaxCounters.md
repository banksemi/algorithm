\[틀림] 문제는 쉽지만 시간 복잡도 최적화가 필요했다.

* 먼저 max\_value를 기억해두고 전체 업데이트가 필요할때 max를 직접 계산하지 않는 것
* \[GPT 도움] 그리고 전체를 업데이트해야할때 직접 하면 O(n)이 소요되니까 base 값만 업데이트해둔다. 나중에 그리고 값을 업데이트하거나 결과를 출력할 때 그때 base를 반영하도록 한다.



```

"""



0으로 시작하는 N개의 카운터



2가지 가능한 동작

\- increase(X): X 카운터를 1 증가

\- max counter - # 모든 카운터를 카운터들의 최대 값 변수로 설정



만약 M개의 숫자가 있는 A가 주어질때(비어있진 않음), 2가지 행동이 있다.

\- if A\[K] == X(1<=X<=N), operation(K): increase(X)

\- if A\[K] == N+1, operation(K) = max\_counter



\# 즉 A\[K]가 1에서 N까지면, 그냥 그 카운터 1 더하라

\# 즉 A\[K]가 N+1 최대값을 넘겼으면, max\_count 하라.



&nbsp;   A\[0] = 3

&nbsp;   A\[1] = 4

&nbsp;   A\[2] = 4

&nbsp;   A\[3] = 6

&nbsp;   A\[4] = 1

&nbsp;   A\[5] = 4

&nbsp;   A\[6] = 4



&nbsp;   (0, 0, 1, 0, 0)

&nbsp;   (0, 0, 1, 1, 0)

&nbsp;   (0, 0, 1, 2, 0)

&nbsp;   (2, 2, 2, 2, 2)

&nbsp;   (3, 2, 2, 2, 2)

&nbsp;   (3, 2, 2, 3, 2)

&nbsp;   (3, 2, 2, 4, 2)



"""

def solution(N, A):

&nbsp;   result = \[0] \* N

&nbsp;   max\_value = 0

&nbsp;   base = 0

&nbsp;   for \_op in A:

&nbsp;       op = \_op - 1

&nbsp;       if op == N:

&nbsp;           base = max\_value

&nbsp;       else:

&nbsp;           if result\[op] < base:

&nbsp;               result\[op] = base

&nbsp;           result\[op] += 1

&nbsp;           if result\[op] > max\_value:

&nbsp;               max\_value = result\[op]

&nbsp;               

&nbsp;   # Implement your solution here

&nbsp;   return \[i if i >= base else base for i in result]



```

