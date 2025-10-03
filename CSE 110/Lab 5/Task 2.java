import java.util.Scanner;
public class Task2{
  public static void main(String [] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the string: ");
    String str1 = sc.nextLine();
    String str2="";
    for (int i=str1.length()-1;i>=0;i--){
    char ch=str1.charAt(i);
    str2+=ch;
    }
    System.out.print(str1.equals(str2));
    }
 }
