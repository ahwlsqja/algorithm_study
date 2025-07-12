import java.util.*;
import java.io.*;

public class week2_10845 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Queue<Integer> q = new LinkedList<>();
        int b = 0;
        
        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String input = st.nextToken();
            
            switch (input) {
                
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    q.add(num);
                    b = num;
                    break;
                    
                case "front":
                    System.out.println(q.isEmpty() ? -1 : q.peek());
                    break;
                    
                case "back":
                    System.out.println(q.isEmpty() ? -1 : b);
                    break;
                    
                case "size":
                    System.out.println(q.size());
                    break;
                    
                case "pop":
                    System.out.println(q.isEmpty() ? -1 : q.poll());  //remove
                    break;   
                    
                case "empty":
                    if(q.isEmpty()){
                        System.out.println("1");
                    } else {
                        System.out.println("0");
                    }
            }
        }
    }
}