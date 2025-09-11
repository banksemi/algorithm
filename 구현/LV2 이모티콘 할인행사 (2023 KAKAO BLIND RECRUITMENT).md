카카오 문제

구현 문제이다. 문제를 차근차근 이해하고 코드로 구현할 수 있는가를 묻는다.

n이 작기 때문에 모든 조합을 직접 고려하면 되고, itertools.product를 떠올렸다.
- 다만 정확한 함수명이 기억이 안나서 dir()으로 조회했지만, 기본적인 것들은 잘 외워두자.

```
"""

두가지 목표가 있다.
- 이모티콘 플러스 가입자 최대한 확보 (우선 목표)
- 이모티콘 판매액 최대한 늘리기

사용자
- 일정 비율 이상 할인하는 이모티콘 모두 구매
- 혹은 이모티콘의 구매 비용 합이 일정 비용을 넘기면, 플러스 서비스에 가입함.

행사 목적을 최대한으로 달성했을 때, 이모티콘 플러스 가입자 수와 이모티콘 매출액을 return

n: 100 이하
이모티콘 할인율: 10, 20, 30, 40
"""
import itertools
from itertools import product
def solution(users, emoticons):
    
    def test(sales): # -> [플러스 가입자 수, 이모티콘 판매액]
        total_plan_registed = 0
        total_price = 0
        for sale_cutoff, accounts in users:
            price = 0
            
            # 일정 할인 이상인 것들을 모두 구매하도록 고려함
            for emoticon_price, sale in zip(emoticons, sales):
                if sale >= sale_cutoff:
                    price += emoticon_price / 100.0 * (100-sale)
            
            # 내 재산보다 구매해야하는 금액이 크거나 같으면
            if price >= accounts:
                total_plan_registed += 1
            else:
                total_price += price
                
        return [total_plan_registed, total_price]
    
    answer = []
    for sales in product([10, 20, 30, 40], repeat=len(emoticons)):
        answer.append(test(sales))
    
    # 가입자 수 우선, 동일한 경우 판매액 우선
    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]



```