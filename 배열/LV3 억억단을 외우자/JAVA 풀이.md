```
import java.util.ArrayList;
import java.lang.*;
import java.util.*;

class Solution {
    public int MAX_NUMBERS = 5_000_000;
    public int[] solution(int e, int[] starts) {
        int[] dp = new int[MAX_NUMBERS+1];

        // 약수 개수 구하기
        for (int i=1;i<=MAX_NUMBERS;i++) {
            for (int j = i; j <= MAX_NUMBERS; j+=i) {
                dp[j] += 1;
            }
        }
        int current_index = e;
        
        Map<Integer, Integer> cache = new HashMap<>();
        for (int i=e; i>0; i--) {
            if (dp[current_index] <= dp[i]) {
                current_index = i;
            }
            cache.put(i, current_index);
        }
        int[] answer = new int[starts.length];
        for (int i=0; i < starts.length;i++) {
            answer[i] = cache.get(starts[i]);
        }
        return answer;
    }
}
```