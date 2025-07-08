import java.util.*;

public class greedy3_11047 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.next());
        int K = sc.nextInt();
        int sum = 0;
        
        int[] arr = new int[N];
        for(int i=0; i<N; i++){
            arr[i] = sc.nextInt();
        }
        sc.close();
        
        for(int i=N-1; i>=0; i--){  //큰 값부터 계산하는 것이 포인트 
            
            sum += K / arr[i];
            K %= arr[i];
        }
        System.out.println(sum);
    }
}