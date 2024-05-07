import java.io.*;
import java.util.*;
public class Main {
    static boolean[] visited;
    static Deque<Integer> stack = new ArrayDeque<>();
    static StringBuilder sb;
    //depth == m
    static void req(int depth, int n){
        int tmp = 999999;
        if(stack.size() == depth){
            for (Integer i : stack) {
                if (tmp  > i){
                    sb.append(i).append(" ");
                    tmp = i;
                }else {
                    sb = new StringBuilder();return;
                }
            }
            sb.reverse().deleteCharAt(0);
            System.out.println(sb);
            sb = new StringBuilder();
        }else {
            for (int i = 1; i <= n; i++) {
                if(!visited[i]){
                    visited[i] = true;
                    stack.push(i);
                    req(depth, n);
                    visited[i] = false;
                    stack.pop();
                }
            }
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), depth = Integer.parseInt(st.nextToken());
        sb = new StringBuilder();  visited = new boolean[n+1];
        req(depth,n);


    }
}
