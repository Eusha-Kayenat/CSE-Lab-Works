import java.util.Scanner;
public class Task1{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the value of n: ");
    int N=sc.nextInt();
    int max=-9999;
    int min=9999;
    int sum=0;
    int average=0;
    int count=0;
    for (int i=1;i<=N;i++){
      System.out.println("Enter a number: ");
      int num=sc.nextInt();
      if (num>=0 && num%2==0){
        sum+=num;
        count+=1;
      if (num<min){
        min=num;
      }
      if(num>max){
         max=num;
      }
      }
    }
      average=sum/count;
      if(sum<0){
      average=0;
      }
    System.out.println("Max: "+max);
    System.out.println("Min: "+min);
    System.out.print("Average: "+average);
   }
}
