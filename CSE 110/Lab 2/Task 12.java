import java.util.Scanner;
public class Task12{
  public static void main (String[]args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the numbers:");
    int x = sc.nextInt();
    int y = sc.nextInt();
    int z = sc.nextInt();
    if (x==y && y==z) {
      System.out.print("All numbers are equal");
    }
    else if (x!=y && y!=z && x!=z){
        System.out.print("All numbers are different");
      }
    else{
        System.out.print("Neither all are equal or different");
      }  
    }
  }
