import java.util.Scanner;
import java.util.Arrays;
public class Task7{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N=sc.nextInt();
    int []array=new int [N];
    int []new_array=new int [N];
    int count=0;

    for (int i=0;i<N;i++){
    System.out.println("Enter a number:");
    int element=sc.nextInt();
    array[i]=element;
    }
    System.out.println("Input array:");
    for (int i=0;i<N;i++){
      if (i==N-1){
      System.out.println(array[i]);
      }
      else{
      System.out.print(array[i]+" ");
     }
    }
    System.out.println("New array:");
    for (int i=0;i<N;i++){
     boolean flag=true;
     for (int j=0;j<count;j++){
       if (new_array[j]==array[i]){
        flag=false;
        break;
       }
     }
     if (flag){
      new_array[j]=array[i];
      count++;
     }
    }
    int []array2=new int [count];
    for (int i = 0; i <array2.length;i++){
    array2[i]=new_array[j];
    }
    for (int i=0;i<N;i++){
    System.out.print(array2[i]+" ");
}
}
}
