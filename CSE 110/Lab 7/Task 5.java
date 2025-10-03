public class Task5{
  public static void showDots(int num){
    for (int i=1;i<=num;i++){
      System.out.print(".");
    }
  }
  public static void show_palindrome(int num){
    for (int i=1;i<=num;i++){
      System.out.print(i);
    }
     for (int i=num-1;i>=1;i--){
      System.out.print(i);
    }
  } 
  public static void showDiamond(int num){
    for (int i=1;i<=num;i++){
     showDots(num-i);
     show_palindrome(i);
     showDots(num-i);
     System.out.println();
    }
    for (int i=num-1;i>=1;i--){
     showDots(num-i);
     show_palindrome(i);
     showDots(num-i);
     System.out.println();
    }
   }
  public static void main(String[]args){
   showDots(5);
   System.out.println();
   show_palindrome(5);
   System.out.println();
   showDiamond(5);
  }
}
