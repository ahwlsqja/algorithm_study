import java.util.*;
import java.io.*;

public class queue_11866 {
    public static void main(String[] args) throws IOException {
        //예시를 보면 3이 지워지고나서 6이 지워지는데
        // 1 2 3x 4 5 6x 7   두칸 넘어 다음 숫자를 지우는 규칙을 발견했다.
        // 마지막은 순서대로 지운다
        //순차적으로 k번째 사람을 지우는 것, 순환 큐인듯 
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i=1; i<=N; i++){
            q.add(i);
        } 
        
        while(!q.isEmpty()){
  
            for(int i=0; i<K; i++){
                if(i == K-1){
                    sb.append(q.poll());
                    if(!q.isEmpty()){
                        sb.append(", ");
                    }
                } else {
                    q.add(q.poll());
                }
            }
        }
        System.out.println("<" + sb + ">");
    }
}