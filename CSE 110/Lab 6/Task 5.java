import java.util.Scanner;
import java.util.Arrays;
public class Task5{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N=sc.nextInt();
    int []array=new int [N];
    boolean flag=false;
      
    for (int i=0;i<N;i++){
    System.out.println("Enter a number:");
    int element=sc.nextInt();
    array[i]=element;
    }
    int num=sc.nextInt();
    for (int i=0;i<N;i++){
     if ((array[i])==num){
     flag=true;
     System.out.print(array[i]+" is at index "+i);
     break;
     }
    }
    if (flag==false){
     System.out.print("Element not found");
    }
  }
}
