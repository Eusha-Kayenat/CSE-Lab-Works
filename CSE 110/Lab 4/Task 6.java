import java.util.Scanner;
public class Task6{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    int div=0;
    for (int i=0;;i++){ 
     System.out.println("Enter a number: ");
     int N=sc.nextInt();
     if (N%2!=0){
       break;
     }
     else if ((N>0) && (N%2==0)){
       div=0;
      for (i=1;i<=N;i++){
       if (N%i==0){
           div+=1;
         }
       }
     System.out.println(N+" has "+div+" divisors");
     }
    }
  }
}
