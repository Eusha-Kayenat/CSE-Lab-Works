import java.util.Scanner;
public class Task7{
  public static void oneToN(int start,int N1){
    if (start>N1){
      return;
    }
     System.out.print(N1+" ");
     oneToN(start+1,N1);
   }
  public static void nToOne(int start,int N2){
    if (start>N2){
      return;
    }
     System.out.print(N2+" ");
     nToOne(start,N2-1);
   }
  public static int recursiveSum(int start,int N3){
    if (start>N3){
      return 0;
    }
     return start+recursiveSum(start+1,N3);
   }
  public static void main(String[]args){
   Scanner sc = new Scanner(System.in);
   System.out.print("Enter the value of N: ");
   int N1 = sc.nextInt(); 
   int N2 = sc.nextInt(); 
   int N3 = sc.nextInt(); 
   oneToN(1,N1);
   nToOne(1,N2);
   recursiveSum(1,N3);
  }
}
