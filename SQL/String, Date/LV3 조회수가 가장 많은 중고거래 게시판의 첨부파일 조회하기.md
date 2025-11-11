문자열 합치기: CONCAT
```
/*
    '조회수가 가장 높은 중고 거래 게시물'에 대한 첨부 파일 경로

가정: 조회수가 가장 높은 게시물은 하나만 존재
출력 형태
/home/grep/src/{BOARD_ID}/{파일ID,파일이름,확장자}

정렬
- FILE ID, 내림차순
*/
WITH MAX_VIEW_POST AS (
    SELECT 
    * 
    FROM 
    USED_GOODS_BOARD 
    WHERE VIEWS=(SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
)

SELECT CONCAT('/home/grep/src/',CAST(BOARD_ID AS CHAR(1000)), '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM
    MAX_VIEW_POST
JOIN
    USED_GOODS_FILE
    USING (BOARD_ID)
ORDER BY FILE_ID DESC
```