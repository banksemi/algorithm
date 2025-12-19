---
URL: https://school.programmers.co.kr/learn/courses/30/lessons/42891
문제 유형:
  - 배열
  - 시뮬레이션
  - 최적화
풀이 날짜: 2025-12-19
정답 여부: 오답
틀린 이유:
  - 논리 오류
  - 시간 초과
  - 최적화
마지막 풀이 날짜:
---
이 문제를 풀 때 최적화 및 논리를 잘못 생각해서 오답이 발생했다.
- time_step을 사용했는데 여기서 더 나아가 코딜리티 최적화 문제처럼 배열의 값을 바로 변경하지 않고 지연 변경하는 최적화 기법을 사용해야한다.
- 이 방법 말고도 우선순위 큐를 사용할 수 있다고 함.

```
"""

1:55 시작

무지가 1초간 음식 섭취하고 남은 음식은 두고 다음 음식을 먹는다. 
- 다음 음식
- 회전판은 마지막 번호 이후에 1번으로 돌아옴.
회전판 시간 없음

food_times 
- 개수: 1~200_000
- 각 원소: 1~100_000_000

빈 접시는 건너뛸 수 있는 최적화 로직이 필요하다.
k = 1 ~ 2 * 10_000_000_000_000
"""

def make_time_steps(seconds):
    """
    시간 배열을 입력받고, 시뮬레이션을 위한 time 간격을 반환한다.
    NlogN
    예시: [1,3,3,10]
    반환: [1,2,0,7]
    """
    sorted_seconds = sorted(seconds)
    result = [sorted_seconds[0]]
    for i in range(1, len(sorted_seconds)):
        result.append(sorted_seconds[i] - sorted_seconds[i-1])
    return result
    
def solution(food_times, k):
    time_steps = make_time_steps(food_times)
    
    # [음식 번호 + 남은 양]
    food_times = [[i+1, v] for i, v in enumerate(food_times)]
    
    offset = 0
    food_count = len(food_times)
    for step in time_steps:
        # 음식 테이블 종류가 변경될 만큼의 시간 여유가 없는 경우 -> break 이 후 직접 시뮬레이션
        if k < step * food_count:
            break
        
        # 음식 테이블이 변경되는 경우
        if step > 0:
            k -= step * food_count
            offset += step
            
        food_count -= 1
            
    new_array = [i for i in food_times if i[1] > offset]
    if new_array:
        return new_array[k % len(new_array)][0]
    else:
        return -1
```