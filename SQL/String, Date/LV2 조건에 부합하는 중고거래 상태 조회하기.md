https://school.programmers.co.kr/learn/courses/30/lessons/164672
```
/*

2022년 10월 5일에 등록된 게시글

거래 상태
- SALE -> 판매중
- RESERVED -> 예약중
- DONE -> 거래완료

정렬 기준
- 게시글 ID, 내림차순
*/

-- 코드를 입력하세요
SELECT 
    BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    CASE
        WHEN STATUS='SALE' THEN '판매중'
        WHEN STATUS='RESERVED' THEN '예약중'
        WHEN STATUS='DONE' THEN '거래완료'
    END AS STATUS
FROM
    USED_GOODS_BOARD
WHERE CREATED_DATE='2022-10-05'
ORDER BY BOARD_ID DESC
```