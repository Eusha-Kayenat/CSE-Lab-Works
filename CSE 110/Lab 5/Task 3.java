import java.util.Scanner;
public class Task3{
  public static void main(String [] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the string: ");
    String str1 = sc.nextLine();
    System.out.print("Enter the character: ");
    char split= sc.nextLine().charAt(0);
    int ascii2=(int)split;
    int count=0;
    int temp=0;
    
    for (int i=0;i<str1.length();i++){
    char ch=str1.charAt(i);
    int ascii1=(int)ch;
    if (ascii1==ascii2){
     for (int j=i-count; j<i ;j++){
    System.out.print(str1.charAt(j));
    }
    System.out.println();
    count=0; 
    temp++;
    } 
    else{
    count++;
    temp++;
    }
    }
    if (temp==(str1.length())){
    for (int i=str1.length()-count; i<str1.length();i++){
    System.out.print(str1.charAt(i));
    }
  }
}
}
