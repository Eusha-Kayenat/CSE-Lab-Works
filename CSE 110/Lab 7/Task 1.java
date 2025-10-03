public class Task1{
  public static void evenChecker(int N){
    if (N%2==0){
    System.out.println("Even!!");
    }
    else{
    System.out.println("Odd!!");
    }
  }
   public static boolean isEven(int N) {
    if (N%2==0){
     return true;
    }
    else{
     return false;
    }
   }

  public static boolean isPos(int N) {
   if (N>=0){
     return true;
    }
   else{
     return false;
    }
  }

  public static void sequence(int n) {
   if (isPos(n)){
    for (int i=0;i<=n;i++){
     if (isEven(i)){
     System.out.print(i+" ");
      }
     }
    System.out.println();
    }
   else{
    for (int i=n;i<=-1;i++) {
     if (!isEven(i)){
     System.out.print(i+ " ");
     }         
    }
    System.out.println();
   }
  }
  public static void main(String[]args){
    evenChecker(10);
    boolean result = isEven(10);
    System.out.println(result);
    boolean result2 = isPos(-5);
    System.out.println(result2);
    sequence(10);
    sequence(-7);
  }
}
