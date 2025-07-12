import java.util.*;
import java.io.*;

public class week2_10828 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        
        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String input = st.nextToken();
            
            switch (input) {
                
                case "push":
                    stack.push(Integer.parseInt(st.nextToken())); 
                    break;   
                    
                case "top":
                    System.out.println(stack.isEmpty() ? -1 : stack.peek());
                    break;
                    
                case "size":
                    System.out.println(stack.size());
                    break;
                    
                case "pop":
                    System.out.println(stack.isEmpty() ? -1 : stack.pop());
                    break;
                
                case "empty":
                    System.out.println(stack.isEmpty() ? 1 : 0);
                    break;
            }
        }
    }
}