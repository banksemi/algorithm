문제를 잘 읽어보면 물고기의 위치가 지정되어있다는 것을 알 수 있다.
따라서 이 경우 스택으로 풀어야했었는데 처음에 문제 조건을 놓쳤다.

문제를 꼼꼼하게 읽자!
```
"""
배열 A, B: N개의 숫자

A: 물고기 크기
B: 방향 (0이면 위, 1이면 아래)
  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0


Then only one fish can stay alive - the larger fish eats the smaller one. 
More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

Initially all the fish are alive and all except fish number 1 are moving upstream. 

Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. 

Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.


물고기 그룹이 2개가 있다. 위쪽, 아래
결국 언젠가는 만나기 때문에 한쪽은 다 잡아먹힌다(크기가 동일한거 빼고)


"""


def solution(A, B):
    stack = []
    result = 0
    for size, i in zip(A, B):
        # 위로 흐르는데 아무것도 없으면
        if i == 0:
            while len(stack):
                # 위로 흐르는 경우 기존 물고기랑 경쟁
                last_item = stack[-1]

                # 아래로 흐르는 물고기가 더 강한 경우
                if last_item > size:
                    break
                
                # 새로운 물고기가 더 강한 경우
                if last_item < size:
                    stack.pop()
            if len(stack) == 0:
                result += 1
        else:
            stack.append(size)
    result += len(stack)
    return result
```