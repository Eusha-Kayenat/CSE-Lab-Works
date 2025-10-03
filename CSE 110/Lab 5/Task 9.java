import java.util.Scanner;
public class Task9{
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.print("Enter the first string: ");
 String pass = sc.nextLine();
 int length = pass.length();
 int count_upper=0;
 int count_lower=0;
 int count_digit=0;
 int count_special=0;
 
 if (length>=8){
 for (int i=0;i<pass.length();i++){
  char ch=pass.charAt(i);
  int ascii=(int)ch;
  if ((ascii>=65 && ascii<=90)||(ascii>=97 && ascii<=122)||(ascii>=48 && ascii<=57)||(ascii==32)){
  if (ascii>=65 && ascii<=90){
   count_upper++;
  }
  if (ascii>=97 && ascii<=122){
   count_lower++;
  }
  if (ascii>=48 && ascii<=57){
    count_digit++;
  }
  }
  else{
    count_special++;
   }
  }
 
 if (count_upper>=1 && count_lower>=1 && count_digit>=1 && count_special>=1){
  System.out.print("True");
 }
 else{
  System.out.print("False"); 
 }
 }
 else{
  System.out.print("False");
 }
 }
}
