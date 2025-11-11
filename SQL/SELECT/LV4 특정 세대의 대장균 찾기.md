https://school.programmers.co.kr/learn/courses/30/lessons/301650

```
WITH RECURSIVE CTE AS (
    SELECT 
        ID, 
        PARENT_ID, 
        1 AS LEVEL 
    FROM 
        ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT 
        ECOLI_DATA.ID, 
        ECOLI_DATA.PARENT_ID, 
        LEVEL + 1 AS LEVEL
    FROM
        ECOLI_DATA
    JOIN
        CTE ON ECOLI_DATA.PARENT_ID=CTE.ID
)

SELECT ID FROM CTE WHERE LEVEL=3 ORDER BY ID

```