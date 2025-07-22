import java.util.*;
import java.io.*;

public class selection_sort1_23881 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        //오름차순으로 선택 정렬
        //선택정렬은 원래 min_index인데. 오름차순이라 max_index를 찾아야했다. 
        int[] arr = new int[N];
        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");

        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st2.nextToken());
        }
    
        int count = 0;
        int max_index = 0;
        int i=0;
        for(i=N-1; i>0; i--){
            max_index = i;
            
            for(int j=i-1; j>=0; j--){
                if(arr[j] > arr[max_index]){
                    max_index = j;  
                }
            }
            
            if(max_index != i){
                //i랑 j 둘다 max인데, 다르면 swap
                //i에 최대값이 담기게됨 
                int temp = arr[max_index];
                arr[max_index] = arr[i];
                arr[i] = temp;
                    
                count++;    //swap후 count 더하기 
                
                if(count == K){
                    break;
                }
            }
        }
        if(count < K){
            System.out.println("-1");
        } else {
            //max_index는 j를 넣은거, 반복문 빠져나와서 어떻게 i ?  미리 선언했음 
            System.out.println(arr[max_index] + " " + arr[i]);
        }
        
    }
}