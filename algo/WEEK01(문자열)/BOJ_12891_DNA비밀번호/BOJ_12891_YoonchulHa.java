import java.io.*;
import java.util.*;

public class Main {
    static int[] myArr = new int[4];
    static int[] ExArr = new int[4];
    static int check = 0;
    public static void Add(char c) {
        switch (c) {
            case 'A': myArr[0]++; if(myArr[0] == ExArr[0]) check++; break;
            case 'C': myArr[1]++; if(myArr[1] == ExArr[1]) check++; break;
            case 'G': myArr[2]++; if(myArr[2] == ExArr[2]) check++; break;
            case 'T': myArr[3]++; if(myArr[3] == ExArr[3]) check++; break;
            default: break;
        }
    }
    public static void Remove(char c) {
        switch (c) {
            case 'A':
                if (myArr[0] == ExArr[0])
                    check--;
                myArr[0]--;
                break;

            case 'C': if (myArr[1] == ExArr[1]) check--; myArr[1]--; break;

            case 'G': if (myArr[2] == ExArr[2]) check--; myArr[2]--; break;

            case 'T': if (myArr[3] == ExArr[3]) check--; myArr[3]--; break;
            default: break;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken()); //윈도우 사이즈
        int result = 0;

        //arrS: 전체 문자열
        char[] arrS = new char[s];

        String str = br.readLine();
        for (int i = 0; i < s; i++) arrS[i] = str.charAt(i);

        st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < 4; i++) {
            ExArr[i] = Integer.parseInt(st.nextToken());
            if (ExArr[i] == 0) check++;
        }

        for (int i = 0; i < p; i++) Add(arrS[i]); // 초기 P 문자열 처리
        if (check == 4) result++;

        for (int i = p; i < s; i++) {
            int j = i - p;
            Add(arrS[i]);
            Remove(arrS[j]);
            if (check == 4) result++;
        }
        System.out.println(result);
    }
}

