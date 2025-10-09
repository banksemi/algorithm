https://school.programmers.co.kr/learn/courses/30/lessons/60060

이 문제는 "LV4 카카오 자동완성"과 유사한 문제로 보인다.
word를 정렬한 다음 이분 탐색을 통해 문제를 풀었다.
**단 이번에도 처음 제출시 런타임 에러가 나왔는데 setrecursionlimit 을 꼭 확인하자**

```
"""
3:19 시작, 3:50 종료
노래 가사에 특정 키워드 몇개 있는지 확인
? -> 한글자 매치

workds: 가사 단어, 중복 없음 2~100000

queries: 검색 키워드 개수 2~100000
- 중복 있음
- ?는 하나 이상 포함되어있으며 앞부분, 뒷부분, 전체 로만 주어짐.

접미사만 먼저 확인한 다음에, 나머지는 문자열 리버스로 찾자.

"""
import sys
sys.setrecursionlimit(2**30)
def solution(words, queries):
    words_with_length = {i: [] for i in range(0, 10001)}
    words_with_length_reversed = {i: [] for i in range(0, 10001)}
    
    for word in words:
        words_with_length[len(word)].append(word)
        words_with_length_reversed[len(word)].append(''.join(reversed(word)))
    
    for i in words_with_length:
        words_with_length[i].sort()
        words_with_length_reversed[i].sort()
        
    def find(words, query, level, min_i, max_i):
        if level == len(query):
            return max_i - min_i
        if query[level] == '?':
            return max_i - min_i
        
        # 물음표가 아닌 경우, 적정 범위를 찾는다.
        query_char = query[level]
        def bsearch(min_i, max_i, left=True):
            if min_i == max_i:
                return min_i
            m = (min_i + max_i) // 2
            m_value = words[m][level]
            if query_char > m_value:
                return bsearch(m+1, max_i, left)
            if query_char < m_value:
                return bsearch(min_i, m, left)
            if query_char == m_value:
                if left:
                    return bsearch(min_i, m, left)
                else:
                    return bsearch(m+1, max_i, left)
        min_i = bsearch(min_i, max_i, left=True)
        max_i = bsearch(min_i, max_i, left=False)
        return find(words, query, level+ 1, min_i, max_i)

    answer = []
    for _query in queries:
        query = _query
        word_dict = words_with_length
        word_length = len(query)
        if _query[0] == '?':# ?로 시작하면 리버스 모드일 수 있음.
            query = ''.join(reversed(query))
            word_dict = words_with_length_reversed
        answer.append(
            find(word_dict[word_length], query, 0, 0, len(word_dict[word_length]))
        )
    return answer
```



풀이 2 - 트라이


트라이 방법으로도 풀 수 있다 다만 위의 이진 탐색보다는 속도가 느리게 나왔다.

```
import sys
sys.setrecursionlimit(2**30)
class Node:
    def __init__(self):
        self.count = 0
        self.childs = {}
    
    def get_child(self, char):
        if char not in self.childs:
            self.childs[char] = Node()
        return self.childs[char]
    
def reverse_word(word):
    return ''.join(reversed(word))

def solution(words, queries):
    root = {i: Node() for i in range(100_001)}
    reversed_root = {i: Node() for i in range(100_001)}
    def dfs(node, word, level):
        node.count += 1
        if level == len(word):
            return
        
        child = node.get_child(word[level])
        dfs(child, word, level + 1)
        
    for word in words:
        length = len(word)
        dfs(root[length], word, 0)
        dfs(reversed_root[length], reverse_word(word), 0)
    
    def find(node, query, level):
        if query[level] == '?':
            return node.count
        if level == len(query):
            return node.count
        
        child = node.get_child(query[level])
        return find(child, query, level + 1)
    answer = []
    for query in queries:
        length = len(query)
        if query.startswith('?'):
            answer.append(find(reversed_root[length], reverse_word(query), 0))
        else:
            answer.append(find(root[length], query, 0))
    return answer
```