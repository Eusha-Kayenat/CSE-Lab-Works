import java.util.Scanner;
import java.util.Arrays;
public class Task2{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the value of N: ");
    int N=sc.nextInt();
    int []array=new int [N];
 
    for (int i=0;i<N;i++){
    System.out.println("Enter an element:");
    int element=sc.nextInt();
    array[i]=element;
    }
    System.out.println("Before removing duplicates:");
    for (int i=0;i<N;i++){
      if (i==N-1){
      System.out.println(array[i]);
      }
      else{
      System.out.print(array[i]+" ");
     }
    }
    System.out.println("After replacing duplicates with 0:");
    for (int i=0;i<array.length;i++){
     for (int j=0;j<array.length;j++){
       if ((i != j) && (array[i] == array[j])){
       array[j] = 0; 
      }
       }
   }
    for (int j=0;j<N;j++){
    System.out.print(array[j]+" ");
    }
  }
}
