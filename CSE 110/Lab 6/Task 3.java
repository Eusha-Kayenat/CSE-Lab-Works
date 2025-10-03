import java.util.Scanner;
import java.util.Arrays;
public class Task3{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N=sc.nextInt();
    int []array=new int [N];
    int []new_array=new int [N];
 
    for (int i=0;i<N;i++){
    System.out.println("Enter a number:");
    int element=sc.nextInt();
    array[i]=element;
    }
    for (int i=0;i<N;i++){
    new_array[i]=array[N-1-i];
     }
   
    System.out.println("Reversed using a new array:");
    for (int i=0;i<N;i++){
      if (i==N-1){
      System.out.println(new_array[i]);
      }
      else{
      System.out.print(new_array[i]+" ");
     }
    }
    
    System.out.println("Reversed the original array:");
    for (int i=0;i<N/2;i++){
     int x=array[i];
     array[i]=array[N-1-i];
     array[N-1-i]=x;
     }
     for (int i=0;i<N;i++){
     System.out.print(array[i]+" ");
    }
  }
}
