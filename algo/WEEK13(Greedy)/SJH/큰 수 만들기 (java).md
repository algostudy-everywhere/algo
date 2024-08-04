import java.util.ArrayList;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        
        ArrayList<Integer> stack=new ArrayList<>();
        
        for (int i=0;i<number.length();i++){
            int digit=number.charAt(i) -'0';
            
            while (!stack.isEmpty() && k>0 && stack.get(stack.size()-1)<digit){
                stack.remove(stack.size()-1);
                k-=1;
                
            }
            stack.add(digit);
            
            
           
        }
        
        while (k>0){
            stack.remove(stack.size()-1);
            k-=1;
        }
        
        for (int num:stack){
            answer+=Integer.toString(num);
        }
        
        return answer;
    }
}