import java.util.*;
import java.io.*;

public class dfs_2667 {
    
    public static int[][] arr;
    public static boolean[][] visited;
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    public static ArrayList<Integer> counter = new ArrayList<>();
    public static int count = 0;
    public static int N;
    
    public static void dfs(int x, int y){
        
        visited[x][y] = true;
        //각 단지내 집의 수를 어떻게 저장할까? dfs()를 할때마다 count++
        count++;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        
        for(int d=0; d<4; d++){
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if(nx >= 0 && ny >= 0 && nx < N && ny < N){
                if(arr[nx][ny] == 1 && !visited[nx][ny]){
                    dfs(nx, ny);
                }
            }
            
        }
        
    }
    public static void main(String[] args) throws IOException {
        //정사각형이므로 N하나만 입력받음
        //그후010101이걸 분리해서 2차원 배열에 저장(br, st유의!!)
        //단지 수를 어떻게 셀 것인가? 1을 전부 단지 수로 바꿔야하나? 그러지않고 count만 하면 될듯
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        visited= new boolean[N][N];
        
        for(int r=0; r<N; r++){
            // StringTokenizer st = new StringTokenizer(br.readLine(), "")
            // 위처럼 사용할 수 없어서 split()해야됨 
            String[] line = br.readLine().split("");
            
            for(int c=0; c<N; c++){
                arr[r][c] = Integer.parseInt(line[c]);
                // System.out.print(arr[r][c]);
            }
        }
        
        for(int r=0; r<N; r++){
            for(int c=0; c<N; c++){
                if(arr[r][c] == 1 && !visited[r][c]){
                    count = 0;  //dfs()전에 count 초기화
                    dfs(r, c);
                    counter.add(count);     //dfs후에 counter에 추가하기 
                }
            }
        }
  
        System.out.println(counter.size());
        Collections.sort(counter);
        for(int c : counter){
            System.out.println(c);
        }
    }
}