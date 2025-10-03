import java.util.Scanner;
public class Task8 {
  public static void reverseDigits(int n) {
    if (n==0){
     return;
    }
    System.out.println(n % 10);
    reverseDigits(n/10);
   }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the value of n: ");
    int n = sc.nextInt(); 
    reverseDigits(n);
  }
}
