import java.util.*;
import java.io.*;
import java.lang.Math;

public class binarySearch_2805 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[n];
        int max = 0;
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            max = Math.max(max, arr[i]);
        }
        
        int start = 0;
        int end = max;
        int result = 0; //답을 저장할 변수 
        while(start <= end){
            
            long total = 0;    //long으로 해야 오버플로우 방지 
            
            int mid = (start + end) / 2;
            for(int i=0; i<n; i++){
                if(arr[i] > mid){
                    total += arr[i] - mid;
                }
            }
            
            if(total >= m){
                //너무 많이 잘림. mid를 늘려야함
                start = mid + 1;
                result = mid;
            } else {
                //너무 덜 잘림. mid를 낮춰서 진행
                end = mid - 1;
            }
        }
        System.out.println(result);
    }
}
