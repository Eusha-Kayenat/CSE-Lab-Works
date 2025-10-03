import java.util.Scanner;
import java.util.Arrays;
public class Task4{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N=sc.nextInt();
    int []array=new int [N];
 
    for (int i=0;i<N;i++){
    System.out.println("Enter a number:");
    int element=sc.nextInt();
    array[i]=element;
    }
    System.out.println("Original array:");
    for (int i=0;i<N;i++){
      if (i==N-1){
      System.out.println(array[i]);
      }
      else{
      System.out.print(array[i]+" ");
     }
    }
    System.out.println("After modifying:");
    
    for (int i=0;i<N;i++){
    if (array[i]>0){
    array[i]=1;
    System.out.print(array[i]+" ");
    }
    else{
    array[i]=0;
    System.out.print(array[i]+" ");
    }
   }
  }
}
