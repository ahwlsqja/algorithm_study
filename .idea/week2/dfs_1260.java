import java.util.*;
import java.io.*;

public class dfs_1260 {
    
    public static boolean[] visited;
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
        
    public static void dfs(int x){
        visited[x] = true;  //현재 노드 방문처리
        System.out.printf("%d ", x);
            
        for(int i=0; i<graph.get(x).size(); i++){
            //노드에 연결된 가야하는 노드 
            int y = graph.get(x).get(i);
            if(!visited[y]){
                dfs(y);
            }
        }
    }
    
    public static void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        
        while(!q.isEmpty()){
            int x = q.poll();
            System.out.printf("%d ", x);    //print()는 매개변수 하나만 사용해서 에러난다.
            
            for(int i=0; i<graph.get(x).size(); i++){
                int y = graph.get(x).get(i);
                
                if(!visited[y]){
                    // bfs(y); 반복문 안이라서 재귀호출하지말고 큐를 활용 
                    q.add(y);
                    visited[y] = true;
                }
            }
        }
    }
        
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());   //정점
        int M = Integer.parseInt(st.nextToken());   //간선
        int V = Integer.parseInt(st.nextToken());   //탐색을 시작할 정점의 번호
        
        visited = new boolean[N+1];
        
        //공간 확보
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        for(int i=0; i<M; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            int from = Integer.parseInt(st2.nextToken());
            int to = Integer.parseInt(st2.nextToken());
            //양방향 그래프 
            graph.get(from).add(to);
            graph.get(to).add(from);
        }
        //정점 번호가 작은 것을 먼저 방문하기 위해 정렬
        for (int i = 0; i <= N; i++) {
            Collections.sort(graph.get(i));
        }
        
        dfs(V);
        System.out.println();
        Arrays.fill(visited, false);
        bfs(V);
    }
}