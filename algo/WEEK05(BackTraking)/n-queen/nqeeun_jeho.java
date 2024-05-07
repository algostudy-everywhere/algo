import java.util.Scanner;

import static java.lang.Math.abs;

public class nqeeun {
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);

        int n=sc.nextInt();
        int[] row=new int[n];


        System.out.println(dfs(0,n,row));



    }

    public static int dfs(int depth,int n,int[] row){
        if (depth==n){
            return 1;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            row[depth] = i;
            if (check(depth, row)) {
                cnt += dfs(depth + 1, n, row); // 해의 수를 증가시키는데 사용
            }
        }
        return cnt; // 현재 깊이에서 가능한 해의 수를 반환
    }




    public static boolean check(int x, int[] row) {
        for (int i = 0; i < x; i++) {
            if ((row[x] == row[i]) || (Math.abs(x - i) == Math.abs(row[x] - row[i]))) {
                return false;
            }
        }
        return true;
    }









}
