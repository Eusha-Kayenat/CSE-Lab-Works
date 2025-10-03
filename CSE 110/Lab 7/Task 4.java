import java.util.Scanner;
public class Task4{
  public static boolean isPrime(int num){
    int div=0;
    for (int i=1;i<=num;i++){
      if (num%i==0){
        div+=1;
      }
    }
      if (div==2){
       return true;
      }
       else{
       return false;
       }
  }  
  public static boolean isPerfect(int num){
    int sum=0;
    for (int i=1;i<=num/2;i++){
     if ((num>0)&&(num %i==0)){
      sum+=i;
     }
    }
     if (sum==num){
      return true;
     }
     else{
      return false;
     }
  }
  public static int special_sum(int num){
    int sum=0;
   for (int i=1;i<=num;i++) {
    if ((isPrime(i)) || (isPerfect(i))){
      sum+=i;
    }
   }
   return sum;
  }
     
  public static void main(String[]args){
   Scanner sc=new Scanner(System.in);
   boolean check = isPrime(7);
   System.out.println(check); 
   boolean check2 = isPerfect(6);
   System.out.println(check2);
   int result = special_sum(sc.nextInt());
   System.out.println(result);
  }
}
