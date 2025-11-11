[틀림] 문제 잘 읽기...


```
/*
자동자 종류: 세단
10월 대여 "시작"기록이 있는 자동차 ID

중복 없어야함
정렬 조건: 자동차 ID 기준 내림차순
*/

SELECT DISTINCT CAR_ID
FROM
    CAR_RENTAL_COMPANY_CAR 
JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    USING (CAR_ID)
WHERE MONTH(START_DATE) = 10 and CAR_TYPE='세단'
ORDER BY CAR_ID DESC
```