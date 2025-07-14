import java.util.*;
import java.io.*;


public class dfs_2606 {

    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    public static boolean[] visited;
    public static int count = 0;
    
    public static void dfs(int x){
        
        visited[x] = true;
        //연결된 컴퓨터 바이러스 어떻게 셀거야 
        for(int i=0; i<graph.get(x).size(); i++){
            int y = graph.get(x).get(i);
            if(!visited[y]){
                dfs(y);
            }
        }
    }
    
    public static void main(String[] args) throws IOException {
        // 깊이 dfs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Node = Integer.parseInt(br.readLine());
        int Edge = Integer.parseInt(br.readLine());
        
        //노드가 1부터시작하는데 array랑 graph는 인덱스 0 부터 시작해서 범위를 Node+1로 한것. 
        for(int i=0; i<=Node; i++){
            graph.add(new ArrayList<>());
        }
        visited = new boolean[Node + 1];
        
        // Node 저장 
        for(int i=0; i<Edge; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph.get(from).add(to);
            graph.get(to).add(from);
        }
        
        dfs(1);
        for(int i=2; i<=Node; i++){
            //1번 제외, 2번부터~
            if(visited[i]){
                count++;
            }
        }
        System.out.println(count);
    }
}