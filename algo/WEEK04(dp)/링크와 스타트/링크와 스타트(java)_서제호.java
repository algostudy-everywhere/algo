
import java.util.Scanner;

import static java.lang.Math.*;

public class backjoon {
    private static int[] visited;
    private static int[][] graph;
    private static int ans;
    private static int n;

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        graph=new int[n][n];
        for (int i=0;i<n;i++ ){
            for (int j=0;j<n;j++){
                graph[i][j]=sc.nextInt();
            }
        }
        visited=new int[n];
        ans=Integer.MAX_VALUE;
        dfs(0,0);
        System.out.println(ans);
        sc.close();
    }

    private static void dfs(int start,int depth){
        if (depth ==(n/2)){
            int a=0;
            int b=0;
            for(int i=0;i<n;i++){
                for(int j=i+1;j<n;j++){
                    if (visited[i]==1 && visited[j]==1){
                        a+=(graph[i][j]+graph[j][i]);
                    } else if (visited[i]==0 && visited[j]==0) {
                        b+=(graph[i][j]+graph[j][i]);
                    }
                }
            }
            ans = Math.min(ans, Math.abs(a - b));
        }
        else{
            for (int i=start;i<n;i++){
                if (visited[i]==0){
                    visited[i]=1;
                    dfs(i+1,depth+1);
                    visited[i]=0;
                }
            }
        }
    }


}
