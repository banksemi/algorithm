https://school.programmers.co.kr/learn/courses/30/lessons/72412


이분 탐색 <- 여기서 시간이 너무 많이 소요됐다.
- 항상 탐색을 할 때 '찾은 값과 목표가 같은 조건'을 어떻게 처리할지 고민하게 된다.
- 차라리 IF를 3개로 나누어, 같을 때 조건을 명확히 명시하면 생각하는데 도움이 되는 것 같다.

```
from dataclasses import dataclass
import copy
@dataclass
class person:
    id: int
    language: str
    position: str
    level: str
    food: str
    score: int
    def __hash__(self):
        return self.id

def parse_person(id, text):
    temp = text.split(' ')
    
    return person(
        id=id,
        language=temp[0],
        position=temp[1],
        level=temp[2],
        food=temp[3],
        score=int(temp[4]),
    )

def parse_query(text):
    temp = text.replace(' and ', ' ')
    return parse_person(0, temp)

from functools import lru_cache
def solution(info, query):
    persons = set(
        parse_person(i, text) for i, text in enumerate(info)
    )
    
    @lru_cache(maxsize=None)
    def search_text(field, value):
        result = set()
        for i in persons:
            if getattr(i, field) == value:
                result.add(i)
        return result
    
    @lru_cache(maxsize=None)
    def search(language, position, level, food):
        result = copy.copy(persons)
        if language != '-':
            result &= search_text('language', language)
        if position != '-':
            result &= search_text('position', position)
        if level != '-':
            result &= search_text('level', level)
        if food != '-':
            result &= search_text('food', food)
        return sorted(result, key=lambda x: x.score)
            
    def bsearch(ppp, min_i, max_i, x):
        m = (min_i + max_i) // 2
        
        if min_i == max_i:
            return m
        if ppp[m].score > x: # 찾은게 목표보다 크다, 그럼 왼쪽 구간에서 탐색
            return bsearch(ppp, min_i, m, x)
        elif ppp[m].score == x: # 찾은게 목표와 같다, 왼쪽으로 탐색
            return bsearch(ppp, min_i, m, x)
        else:
            return bsearch(ppp, m+1, max_i, x)
        
    answer = []
    for text in query:
        q = parse_query(text)
        result = search(q.language, q.position, q.level, q.food)
        c = len(result) - bsearch(result, 0, len(result), q.score)
        answer.append(c)
    return answer
```