import java.util.*;
class Solution {
    public int solution(int[] properties, int location) {
        Queue<int[]> q = new LinkedList<>();
        Queue<int[]> ans = new LinkedList<>();
        for (int i = 0; i < properties.length; i++) {
            int[] prop = {i, properties[i]};
            q.add(prop);
        }
        Arrays.sort(properties);
        int max = properties[properties.length - 1];
        int min = properties[0];
        int curr = q.peek()[1]; int cnt = 1;
        while(!q.isEmpty()) {
            int[] tmp = q.poll();
            curr = tmp[1];
            if(curr == max){
                ans.add(tmp);
            } else q.add(tmp);

            if(max == min){
                while (!q.isEmpty()) {
                    ans.add(q.poll());
                }break;
            }
            max = properties[q.size()-1];
        }
        int loc = 1;
        while(!ans.isEmpty()){
            if(ans.poll()[0] == location) break;
            loc++;
        }
        return loc;
    }
}
