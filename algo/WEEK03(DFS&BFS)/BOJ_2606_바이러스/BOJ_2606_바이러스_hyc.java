import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        StringTokenizer st;
        boolean[] isVisited = new boolean[n+1];
        HashSet<Integer>[] arr = new HashSet[n+1];
        for (int i = 1; i < n+1; i++) arr[i] = new HashSet<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b); arr[b].add(a);
        }
        Stack<Integer> stack = new Stack<>();
        stack.add(1);
        stack.addAll(arr[1]); int curr = 1, cnt = 0;
        while(!stack.isEmpty()){
            curr = stack.pop();
            if (!isVisited[curr]){
                cnt++; isVisited[curr] = true;
                stack.addAll(arr[curr]);
            }
        }
        System.out.println(cnt-1);
    }
}
