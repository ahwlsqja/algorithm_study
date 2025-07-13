import java.util.*;
import java.io.*;

class Document{
    int index;
    int priority;
    
    Document(int index, int priority){
        this.index = index;
        this.priority = priority;
    }
}

public class queue_1966 {
    public static void main(String[] args) throws IOException {
        // T
        // N 문서의 개수,  M: M번째에 있다. (0부터 시작)
        // 중요도
         
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int M = Integer.parseInt(st.nextToken());
            int index = Integer.parseInt(st.nextToken());
            
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            Queue<Document> q = new LinkedList<>();
            PriorityQueue<Integer> pQ = new PriorityQueue<>(Collections.reverseOrder());
            int count = 0;
            int result = 0;
            
            for(int j=0; j<M; j++){
                int num = Integer.parseInt(st2.nextToken());
                pQ.add(num); //중요도
                q.add(new Document(j, num));
                // if(index == j){
                    // find = num;
                // }
            }
            while(!q.isEmpty()){
                
                Document d = q.poll();  //하나 먼저 꺼내서 우선순위(중요도) 비교 
                if(d.priority < pQ.peek()) {
                    //뒤로 넘기기
                    q.add(d);
                } else {
                    pQ.poll();
                    count++;
                    if(d.index == index){   //찾아야햇던 수의 index랑 같다면
                        result = count;
                        break;
                    }
                }
            }
            System.out.println(result);
        }
    }
}


