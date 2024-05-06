import java.util.Scanner;

public class sticker_path {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        int[][] onebon = new int[n][m];


        for (int t = 0; t < k; t++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int[][] sticker = new int[a][b];
            for (int x = 0; x < a; x++) {
                for (int y = 0; y < b; y++) {
                    sticker[x][y] = sc.nextInt();
                }
            }


            boolean visited = false;
            int cnt = 0;
            while (cnt < 4) {
                if (visited) {
                    break;
                }
                for (int i = 0; i < n - sticker.length + 1; i++) {
                    if (visited == true)
                        break;
                    for (int j = 0; j < m - sticker[0].length + 1; j++) {
                        if (check(onebon, sticker, i, j)) {
                            attach(onebon, sticker, i, j);
                            visited = true;
                            break;
                        }
                    }
                }
                sticker = do90(sticker);
                cnt += 1;
            }
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ans += onebon[i][j];
            }
        }

        System.out.println(ans);

    }


    public static int[][] do90(int[][] sticker) {
        int r = sticker.length;
        int c = sticker[0].length;

        int[][] new_sticker = new int[c][r];
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                new_sticker[i][j] = sticker[r - j - 1][i];
            }
        }
        return new_sticker;
    }

    public static int[][] attach(int[][] onebon, int[][] sticker, int x, int y) {
        int r = sticker.length;
        int c = sticker[0].length;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                onebon[x + i][y + j] += sticker[i][j];

            }
        }
        return onebon;
    }

    public static boolean check(int[][] onebon, int[][] sticker, int x, int y) {
        int r = sticker.length;
        int c = sticker[0].length;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (onebon[x + i][y + j] + sticker[i][j] > 1) {
                    return false;
                }
            }
        }
        return true;
    }

}

