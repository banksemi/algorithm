https://school.programmers.co.kr/learn/courses/30/lessons/1832

JAVA 만 지원하므로 python 답안 작성 후 JAVA 컨버팅
점화식을 통해 경우의 수를 구하는 공식을 먼저 작성함.

y-1, x 타일에서 y,x 타일로 올 수 있는데, y-1,x 타일이 회전 금지인 경우 y-1,x 타일에 '세로 방향'으로 도착한 경우의 수만 사용 가능하다.



```
"""
3:10 시작 3:31
1 <= m, n <= 500
0: 자유
1: 통행 금지
2: 회전 금지

자동차는 오른쪽 또는 아래 방향으로 한 칸씩 이동 가능하다.
도시의 도로 상태가 입력으로 주어졌을 때, 왼쪽 위의 출발점에서 오른쪽 아래 도착점까지 자동차로 이동 가능한 전체 가능한 경로 수를 출력하는 프로그램을 작성하라. 이때 가능한 경로의 수는 컴퓨터가 표현할 수 있는 정수의 범위를 넘어설 수 있으므로, 가능한 경로 수를 20170805로 나눈 나머지 값을 출력하라.

항상 위나 왼쪽에서 올 수 있다.

if 0 or 2:
    dp[y][x][FROM_TOP] = if (y-1, x) == 2 dp[y-1][x][FROM_TOP] else dp[y-1][x][ALL]
    dp[y][x][FROM_LEFT] =  if (y, x-1) == 2 dp[y][x-1][FROM_LEFT] else dp[y][x-1][ALL]
    dp[y][x][ALL] = dp[y][x][FROM_TOP] + dp[y][x][FROM_LEFT]
if 1:
    dp[y][x][FROM_TOP] = 0
    dp[y][x][FROM_LEFT] = 0
    dp[y][x][ALL] = 0
"""
def solution(m, n, city_map):
    FROM_TOP = 0
    FROM_LEFT = 1
    ALL = 2
    dp = {}
    dp[(0, 0, FROM_LEFT)] = 1
    dp[(0, 0, FROM_TOP)] = 1
    dp[(0, 0, ALL)] = 1

    for y in range(m):
        for x in range(n):
            if y == 0 and x == 0:
                continue
            if city_map[y][x] == 1:
                dp[(y, x, FROM_TOP)] = 0
                dp[(y, x, FROM_LEFT)] = 0
                dp[(y, x, ALL)] = 0
                continue

            if y == 0:
                dp[(y, x, FROM_TOP)] = 0
            else:
                if city_map[y-1][x] == 2:
                    dp[(y, x, FROM_TOP)] = dp[(y-1, x, FROM_TOP)]
                else:
                    dp[(y, x, FROM_TOP)] = dp[(y-1, x, ALL)]

            if x == 0:
                dp[(y, x, FROM_LEFT)] = 0
            else:
                if city_map[y][x-1] == 2:
                    dp[(y, x, FROM_LEFT)] = dp[(y, x-1, FROM_LEFT)]
                else:
                    dp[(y, x, FROM_LEFT)] = dp[(y, x-1, ALL)]
            dp[(y, x, FROM_TOP)] = dp[(y, x, FROM_TOP)] % 20170805
            dp[(y, x, FROM_LEFT)] = dp[(y, x, FROM_LEFT)] % 20170805
            dp[(y, x, ALL)] = (dp[(y, x, FROM_TOP)] + dp[(y, x, FROM_LEFT)])  % 20170805
    return dp[(m-1,n-1, ALL)]
assert solution(3,3,[[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 6
assert solution(3,6,[[0, 2, 0, 0, 0, 2], [0, 0, 2, 0, 1, 0], [1, 0, 0, 2, 2, 0]]) == 2
```


```
class Solution {
    public int solution(int m, int n, int[][] city_map) {
        final int FROM_TOP = 0;
        final int FROM_LEFT = 1;
        final int ALL = 2;
        final int MOD = 20170805;

        int[][][] dp = new int[m][n][3];

        dp[0][0][FROM_LEFT] = 1;
        dp[0][0][FROM_TOP] = 1;
        dp[0][0][ALL] = 1;

        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (y == 0 && x == 0) {
                    continue;
                }
                if (city_map[y][x] == 1) {
                    dp[y][x][FROM_TOP] = 0;
                    dp[y][x][FROM_LEFT] = 0;
                    dp[y][x][ALL] = 0;
                    continue;
                }

                if (y == 0) {
                    dp[y][x][FROM_TOP] = 0;
                } else {
                    if (city_map[y - 1][x] == 2) {
                        dp[y][x][FROM_TOP] = dp[y - 1][x][FROM_TOP];
                    } else {
                        dp[y][x][FROM_TOP] = dp[y - 1][x][ALL];
                    }
                }

                if (x == 0) {
                    dp[y][x][FROM_LEFT] = 0;
                } else {
                    if (city_map[y][x - 1] == 2) {
                        dp[y][x][FROM_LEFT] = dp[y][x - 1][FROM_LEFT];
                    } else {
                        dp[y][x][FROM_LEFT] = dp[y][x - 1][ALL];
                    }
                }
                
                dp[y][x][FROM_TOP] = dp[y][x][FROM_TOP] % MOD;
                dp[y][x][FROM_LEFT] = dp[y][x][FROM_LEFT] % MOD;
                dp[y][x][ALL] = (dp[y][x][FROM_TOP] + dp[y][x][FROM_LEFT]) % MOD;
            }
        }
        return dp[m - 1][n - 1][ALL];
    }
}
```