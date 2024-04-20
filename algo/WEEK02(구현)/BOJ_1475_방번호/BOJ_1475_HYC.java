import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] ch = String.valueOf(br.readLine()).toCharArray();
        int[] howmuch = new int[9];
        int cnt = 0;
        for (char c : ch) {
            if(c == '6' || c == '9') cnt++;
            else howmuch[c - '0']++;
            if(cnt == 2){ howmuch[6]++; cnt = 0;}
        }
        if(cnt == 1) howmuch[6]++;
        Arrays.sort(howmuch);
        System.out.println(howmuch[8]);
    }
}