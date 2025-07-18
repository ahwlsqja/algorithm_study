import java.util.*;
import java.io.*;

public class dfs_11724 {
    
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    public static boolean[] visited;
    public static int count = 0;
    
    public static void dfs(int x){
        visited[x] = true;
        
        for(int i=0; i<graph.get(x).size(); i++){
            int y = graph.get(x).get(i);
            if(!visited[y]){
                dfs(y);
            }        
        }    
    }
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        visited = new boolean[N+1];
        
        //정점만큼 공간 확보
        for(int i=0; i<=N; i++){
            graph.add(new ArrayList<>());
        }
        
        //간선
        for(int j=0; j<M; j++){
            //방향이 없다? => 양방향 가능해서 두줄 넣기 
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            int from = Integer.parseInt(st2.nextToken());
            int to = Integer.parseInt(st2.nextToken());
            graph.get(from).add(to);    //방향이 있다면 이것만 
            graph.get(to).add(from);
        }
        
        //정점 1~6
        for(int j=1; j<=N; j++){
            if(!visited[j]){
                dfs(j);
                count++;
            }
        }
        
        System.out.println(count);
    }
}