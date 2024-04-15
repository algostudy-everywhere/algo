import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            char[] ch = br.readLine().toCharArray();
            HashSet<Character> set = new HashSet<>();
            char pr = ch[0];
            for (int j = 0; j < ch.length; j++) {
                if(set.contains(ch[j]) && pr != ch[j]) break;
                else {
                    set.add(ch[j]);
                    pr = ch[j];
                }
                if( j == ch.length-1) cnt++;
            }
        }
        System.out.println(cnt);
    }
}