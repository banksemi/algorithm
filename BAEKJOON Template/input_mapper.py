from collections import deque
queue = deque()

with open("test-case.txt", "r") as f:
    for i in f.readlines():
        queue.append(i.strip())

def input():
    return queue.popleft()