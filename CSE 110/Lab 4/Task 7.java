import java.util.Scanner;
public class Task7{
  public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int sum = 0;
    for(int i=0;i<N;i++){
      int x = sc.nextInt();
      int y = sc.nextInt();
      if(x%2==0){
        x+=1;
      }
      for(int j=1;j<=y;j++){
         sum +=x;
         x+=2;
      }
      System.out.println(sum);
      
    }
  }
  }
