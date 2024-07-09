![image](https://github.com/algostudy-everywhere/algo/assets/93638922/9fc30057-2b42-4e4b-82a3-45b376566609)


```java
import java.util.*;

class Solution {
    int sum(Queue<Integer> q){
        int sum = 0;
        for(int i : q) sum+=i;
        return sum;
    }
    
    public int solution(int[] queue1, int[] queue2) {
        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        int sum = 0;
        int cnt = 0;
        int max = 0;

        for (int i : queue1){
            q1.offer(i);
            sum+=i;
            if(max < i) max = i;
        }
        for (int i : queue2){
            q2.offer(i);
            sum+=i;
            if(max < i) max = i;
        }
        if(sum % 2 != 0) return -1;
        if(max > sum/2)return -1;
        int q1Sum, q2Sum;
        while(sum(q1) != sum/2){
            q1Sum = sum(q1); q2Sum = sum(q2);
            if(q1Sum == q2Sum){
                return cnt;
            }
            else if(q1Sum > q2Sum){
                q2.offer(q1.poll());
                cnt++;
            }else{
                q1.offer(q2.poll());
                cnt++;
            }
            
        }
        return cnt;
    }
}
```
