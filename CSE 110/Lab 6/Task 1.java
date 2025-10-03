import java.util.Scanner;
import java.util.Arrays;
public class Task1{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the value of N: ");
    int N=sc.nextInt();
    int []array=new int [N];
    System.out.println("The elements of the array are:");
    for (int i=0;i<N;i++){
     System.out.println("Enter a number: ");
     int element1=sc.nextInt();
     array[i]=element1;
     System.out.println(i+":"+element1);
    }
    System.out.println("Enter another number: ");
    int element2=sc.nextInt();
    int []b=new int [N+1];
     for (int i=0;i<array.length;i++){
      b[i]=array[i];
     }
    b[b.length-1]=element2;
   
    System.out.println("After resizing the array: ");
    for (int i=0;i<b.length;i++){
    System.out.print(b[i]+" ");
    }
  }
}
