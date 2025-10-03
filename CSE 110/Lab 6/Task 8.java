import java.util.Scanner;
import java.util.Arrays;
public class Task8{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Please enter the length of array 1:");
    int N1=sc.nextInt();
    int []array1=new int [N1];
    System.out.println("Please enter the elements of arr1: ");
    
    for (int i=0;i<N1;i++){
    array1[i]=sc.nextInt();
    }
    System.out.println("Please enter the length of array 2:");
    int N2=sc.nextInt();
    int []array2=new int [N2];
    System.out.println("Please enter the elements of arr2:");
    
    for (int i=0;i<N2;i++){
    array2[i]=sc.nextInt();
    }
    boolean subset = true;
    for (int i=0;i<N2;i++){
    boolean found = false;
     for (int j=0;j<N1;j++) {
      if (array2[i] == array1[j]) {
      found = true;
      break;
      }
     }
      if (!found) {
      subset = false;
      break;
      }
     }

     if (subset) {
     System.out.print("Array 2 is a subset of Array 1.");
     } 
     else{
     System.out.print("Array 2 is not a subset of Array 1.");
     }
    }
}
