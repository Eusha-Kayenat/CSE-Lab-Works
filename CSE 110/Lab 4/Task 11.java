import java.util.Scanner;
public class Task11{
  public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a number: ");
    int start = sc.nextInt();
    System.out.println("Enter a number: ");
    int end = sc.nextInt();
    int count = 0;
    int x = start;
    int z = 0;
    while(x!=0){
      z = x%10;
      count++;
      x/=10;
    }
    System.out.println("Armstrong numbers: ");
    for(int i=start;i<=end;i++){
      int sum = 0;
      int p = i;
      while(p!=0){
        int y = 0;
        y = p%10;
        sum+= Math.pow(y,count);
        p/=10;
      }
      if(sum==i){
        System.out.println(i);
      }
    }
  }
}
