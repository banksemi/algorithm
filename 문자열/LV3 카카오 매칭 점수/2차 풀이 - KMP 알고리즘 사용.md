https://school.programmers.co.kr/learn/courses/30/lessons/42893

문자열 매칭 부분을 KMP 알고리즘으로 구현한 버전

```
"""
from string import ascii_uppercase
from functools import lru_cache
from collections import defaultdict
ABC = set(ascii_uppercase)

@lru_cache(maxsize=None)
def kmp_pattern(text):
    arr = [0] * len(text)
    j = 0
    for i in range(1, len(text)):
        while j != 0 and text[i] != text[j]:
            j = arr[j-1]
        
        if text[i] == text[j]:
            j += 1
            arr[i] = j
    return arr

def text_match(text, keyword, offset=0):
    keyword_pattern = kmp_pattern(keyword)
    
    j = 0
    for i in range(offset, len(text)):
        while j != 0 and text[i] != keyword[j]:
            j = keyword_pattern[j-1]
        if text[i] == keyword[j]:
            j += 1
            if j == len(keyword):
                start = i - j + 1
                yield (start, start + len(keyword))
                j = keyword_pattern[j-1]
    
def get_base_score(text, keyword):
    text = text.upper()
    keyword = keyword.upper()
    score = 0
    j = 0
    for start, end in text_match(text, keyword):
        if start > 0 and text[start-1] in ABC:
            continue
        if end < len(text) and text[end] in ABC:
            continue
        score += 1
    return score
    
def get_text(text, keyword, end_keyword):
    for start, end in text_match(text, keyword):
        for start2, end2 in text_match(text, end_keyword, offset=end):
            # end를 찾으면 바로 종료 후, 다음 키워드 탐색
            yield text[start:end2]
            break
    
def find_tag(page, tag_name, attribute, requires_word=None):
    for meta_text in get_text(page, '<' + tag_name, '>'):
        if requires_word and not requires_word in meta_text:
            continue
            
        for aaa in get_text(meta_text, attribute+'="', '"'):
            yield aaa.split('"')[1]

def get_base_url(page):
    for url in find_tag(page, 'meta', 'content', 'property="og:url"'):
        return url
    return None

def get_links(page):
    result = []
    for meta_text in get_text(page, '<a', '</a>'):
        for aaa in get_text(meta_text, 'href="', '"'):
            result.append(aaa.split('"')[1])
    return result

def solution(word, pages):
    scores = defaultdict(dict)
    htmls = {}
    
    for page in pages:
        url = get_base_url(page)
        if url is None:
            break # 테스트 코드에 영향이 없음
        htmls[url] = page
        scores[url] = {
            'base': get_base_score(page, word),
            'links': get_links(htmls[url]),
            'refered': []
        }
    for url in scores:
        for link in scores[url]['links']:
            if link in scores:
                scores[link]['refered'].append(url)
        
    for url in scores:
        link_score = 0
        for refer in scores[url]['refered']:
            if refer in scores:
                link_score += scores[refer]['base'] / len(scores[refer]['links'])
        scores[url]['link'] = link_score
        scores[url]['total'] = scores[url]['base'] + scores[url]['link']

    # 매칭 점수가 가장 큰거
    max_score = max([i['total'] for i in scores.values()])

    for i, data in enumerate(scores.values()):
        if data['total'] == max_score:
            return i
    answer = 0
    return answer
```