import java.util.Scanner;
import java.util.Arrays;
public class Task6{
  public static void main (String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N=sc.nextInt();
    double []array=new double [N];
    double max=-9999;
    double min=9999;
    double sum=0;

    for (int i=0;i<N;i++){
    System.out.println("Enter a number:");
    double element=sc.nextDouble();
    array[i]=element;
    sum+=element;
    }
    for (int i=0;i<N;i++){
    double num=array[i];

     if (num<min){
        min=num;
      }
     if(num>max){
         max=num;
      }
     }
    for (int i=0;i<N;i++){
     if ((array[i])==max){
     System.out.println("Maximum element "+array[i]+" found at index "+i);
     break;
     }
    }
    for (int i=0;i<N;i++){
     if ((array[i])==min){
     System.out.println("Minimum element "+array[i]+" found at index "+i);
     break;
     }
    }
     
    double average=sum/N;
    System.out.println("Summation: "+sum);
    System.out.print("Average: "+average);
   }
}
