import java.util.Scanner;

public class CustomParitySort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();          
        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
            
        while (true) {
            boolean val = false;

            for (int i = 0; i < n - 1; i++) {
                if (arr[i] % 2 == arr[i + 1] % 2 && arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    val = true;
                }
            }

            if (!val) {
                break; 
            }
        }
        for (int num : arr)
            System.out.print(num + " ");
    }
}
