누적합을 사용했다.

근데 문제에서 요구하는건 구간 내에 있는 최소 값이다.

단 값의 범위가 1~4로 한정되어있기 때문에 '1'의 개수 누적합, '2'의 개수 누적합 이런식으로 응용해서 문제를 풀었다.


```
"""
DNA 순서는 A, C, G, T 로 표현된다

A -> 1
C -> 2
G -> 3
T -> 4

여러 쿼리? impact factor가 최소화되는 DNA 순서를 찾아야한다.

S: N(1~10만) 글자수
P,Q: M(50000)개의 배열

M개의 쿼리 K-th Query (0<=K<M)

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
    S = CAGCCTA

즉 P Q가 범위다. 
- 2,4면 2,3,4
- 5,5면 5,5

"""

def solution(S, P, Q):
    # Implement your solution here
    # 일단 문자열을 숫자로 바꾸자.
    # CAG -> 213...

    # 즉 특정 범위에서 최소값 구하는 문제. 
    # 누적합 -> 1,2,3,4 각각의 개수 합이라고 생각하자

    array = []
    for i in S:
        if i == 'A':
            array.append(1)
        if i == 'C':
            array.append(2)
        if i == 'G':
            array.append(3)
        if i == 'T':
            array.append(4)
    
    # 누적합 테이블을 만들자.
    sum_table = {
        i: [0] * len(S) for i in range(1, 5)
    }
    
    for i, number in enumerate(array):
        for table_num in range(1, 5):
            if i != 0:
                sum_table[table_num][i] = sum_table[table_num][i - 1]

            if table_num == number:
                sum_table[table_num][i] += 1
    
    def find(p, q):
        # p랑 q를 포함하는 테이블
        for i in range(1, 5):
            temp = sum_table[i][q]
            if p != 0:
                temp -= sum_table[i][p-1]
            if temp > 0:
                return i
    result = []
    for p, q in zip(P, Q):
        result.append(find(p, q))
    return result
```