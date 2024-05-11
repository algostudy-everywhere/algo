import java.util.ArrayList;
import java.util.Scanner;

public class truck {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int n=sc.nextInt();
        int w=sc.nextInt();
        int L=sc.nextInt();

        ArrayList<Integer> truck=new ArrayList<>();

        for (int i=0;i<n;i++){
            truck.add(sc.nextInt());
        }

        ArrayList<Integer> bridge=new ArrayList<>();
        for (int i=0;i<w;i++){
            bridge.add(0);
        }
        int time=0;

        while (bridge.size()!=0){
            int sum=0;
            time+=1;
            bridge.remove(0);
            if (truck.size()!=0){
                for (int i=0;i<bridge.size();i++){
                    sum+=bridge.get(i);
                }
                if ((sum+truck.get(0))<=L){
                    bridge.add(truck.get(0));
                    truck.remove(0);
                }
                else{
                    bridge.add(0);
                }
            }

        }
        System.out.println(time);




    }
}
