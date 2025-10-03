import java.util.Scanner;
import java.util.Arrays;
public class Task10{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N=sc.nextInt();
    int []marks=new int [N];
    String []names=new String [N];

    for (int i=0;i<N;i++){
    System.out.println("Enter a number:");
    marks[i]=sc.nextInt();
    }
    for (int i=0;i<N;i++){
    System.out.println("Enter a name:");
    names[i]=sc.nextLine();
    }
    System.out.println("Sorted array:");
    
    for (int i=0;i<N;i++){
      int min=i;
      for (int j=i+1;j<N;j++){
        if (marks[min]>marks[j]){
        min=j;
        }
      }
      int temp = marks[i];
      marks[i] = marks[min];
      marks[min]=temp;
      
    }
    for (int i=0;i<N;i++){
      if (i==N-1){
      System.out.println(marks[i]);
      }
      else{
      System.out.print(marks[i]+" ");
     }
    }
    for (int i=0;i<N;i++){
    System.out.print(names[i]+" ");  
    }
  } 
}
