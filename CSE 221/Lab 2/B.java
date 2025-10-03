import java.util.*;
public class Two_Sum_Revisited{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);     
        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[M];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        for (int j = 0; j < M; j++) {
            B[j] = sc.nextInt();
        }
        int i = 0; 
        int j = M - 1;    

        int minDiff = Integer.MAX_VALUE;
        int bestI = 0;
        int bestJ = 0;

        while (i < N && j >= 0) {
            int sum = A[i] + B[j];
            int diff = Math.abs(sum - K);

            if (diff < minDiff) {
                minDiff = diff;
                bestI = i;
                bestJ = j;
            }

            if (sum < K) {
                i++;
            } else if (sum > K) {
                j--;
            } else {
                break;
            }
        }
        System.out.println((bestI + 1) + " " + (bestJ + 1));
    }
}
