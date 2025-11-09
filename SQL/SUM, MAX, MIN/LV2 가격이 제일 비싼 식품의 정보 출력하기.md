
**MAX 값을 먼저 알아낸 후 사용하는 방법**
```
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE FROM FOOD_PRODUCT join (SELECT max(PRICE) as MAX_PRICE from FOOD_PRODUCT) AS B where FOOD_PRODUCT.PRICE = MAX_PRICE;
```

WHERE에서 직접 서브쿼리를 사용하면 모든 rows에 대해 중복 연산이 발생할 가능성이 있다고 생각되어 값을 먼저 구한 뒤 JOIN을 통해 연결했다.

**WHERE에서 직접 SELECT를 계산하면서 반복 조회**
```
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE FROM FOOD_PRODUCT where PRICE = (SELECT max(PRICE) FROM FOOD_PRODUCT);
```

**정렬을 사용하는 방법(주의)**
```
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE FROM FOOD_PRODUCT ORDER BY PRICE DESC LIMIT 1;
```
정렬을 통해서 문제를 풀 수도 있지만, 인덱스가 없는 경우 시간 복잡도가 증가하며, 동일한 PRICE를 가진 제품이 2개 이상인 케이스가 있는 경우 사용할 수 없다.

