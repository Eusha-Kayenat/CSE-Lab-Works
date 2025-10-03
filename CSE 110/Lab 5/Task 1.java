import java.util.Scanner;
public class Task1{
  public static void main(String [] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the string: ");
    String str1 = sc.nextLine();
    String str2="";
    for (int i=0;i<str1.length();i++){
    char ch=str1.charAt(i);
    int ascii=(int)ch;
    if (ascii>=97 && ascii<=122){
      int new_ascii=ascii-32;
      char new_ch=(char)new_ascii;
      str2+=new_ch;
      
    }
    else{
      str2+=ch;
    }
   }
    System.out.print(str2);
 }
}
