import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 정수삼각형 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); 
        sc.nextLine();

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            String[] numbers = line.split("\\s+"); 
            ArrayList<Integer> row = new ArrayList<>();

            for (String number : numbers) {
                row.add(Integer.parseInt(number));
            }
            graph.add(row);
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < graph.get(i).size(); j++) {
                if (j == 0) {
                    graph.get(i).set(j, graph.get(i).get(j) + graph.get(i - 1).get(j));
                } else if (j == (graph.get(i).size() - 1)) {
                    graph.get(i).set(j, graph.get(i).get(j) + graph.get(i - 1).get(j - 1));
                } else {
                    graph.get(i).set(j, graph.get(i).get(j) + Math.max(graph.get(i - 1).get(j - 1), graph.get(i - 1).get(j)));
                }
            }
        }

        System.out.println(Collections.max(graph.get(n - 1)));
        sc.close();
    }
}

