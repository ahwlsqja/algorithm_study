import java.util.*;

public class greedy2_11399 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        
        for(int i=0; i<N; i++){
            arr[i] = sc.nextInt();    
        }
        sc.close();
        
        Arrays.sort(arr);
        int sum = arr[0];
        int total = sum;
        
        for(int j=1; j<N; j++){
            sum += arr[j];
            total += sum;
        }
        
        System.out.println(total);
        // 3 1 4 3 2
        // 3, 4, 8, 11, 13 = 39
        // 1 2 3 3 4
        // 1, 3, 6, 9, 13 = 32
        
    }
}
