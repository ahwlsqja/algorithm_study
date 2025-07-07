// 여2 남1 
// 여N 남M 인턴쉽에참가해야하는 학생은 참가 못함 K
import java.util.*;
import java.io.*;

public class greedy1_2875 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int team = 0;
        
        while(N>=2 && M>=1 && (N + M - K >= 3)){
            team++;
            N -= 2;
            M--;
        }
        System.out.println(team);
    }
}