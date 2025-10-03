import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); 
        
        for (int i = 0; i < T; i++) {
            long N = sc.nextLong(); 
            long sum = N * (N + 1) / 2;
            System.out.println(sum);
        }
    }
}
