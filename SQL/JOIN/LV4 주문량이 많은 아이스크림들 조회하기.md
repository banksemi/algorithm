
먼저 JULY 테이블에서는 아이스크림 생산량이 많아 같은 맛이 2개 이상의 출하 번호를 가진다고 한다. 따라서 GROUP BY FLAVOR을 통해 생산량을 묶어준다.

그리고 만들어진 그룹과 FIRST_HALF을 JOIN하여 같은 'FLAVOR' 끼리 연결하고 합을 구했다. 

```
# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

SELECT FLAVOR FROM
(
    SELECT A.FLAVOR, TOTAL_ORDER+TOTAL_ORDER2 as SUM_ORDER
    FROM
        FIRST_HALF as A
    JOIN
        (
            SELECT FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER2 FROM JULY GROUP BY FLAVOR
        ) as B
    ON A.FLAVOR = B.FLAVOR
    ORDER BY SUM_ORDER DESC
    LIMIT 3
) AS C
```