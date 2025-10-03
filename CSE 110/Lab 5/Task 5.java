import java.util.Scanner;
public class Task5{
 public static void main(String [] args){
  Scanner sc = new Scanner(System.in);
  System.out.print("Enter the string: ");
  String str = sc.nextLine();
  int vowel=0;
  int consonant=0;
  
  for (int i=0;i<str.length();i++){
  char ch=str.charAt(i);
  int ascii=(int)ch;
  if ((ascii>=65 && ascii<=90)||(ascii>=97 && ascii<=122)){
  if (ascii==97||ascii==101||ascii==105||ascii==111||ascii==117){
  vowel++;
  }
  else{
  consonant++;
  }
  }
  }
  if (vowel>0 && consonant>0){
  if((vowel%3==0) && (consonant%5==0)){
  System.out.print("Aaarr! Me Plunder!!");
  }
  else{
  System.out.print("Blimey! No Plunder!!");
  }
  }
  else{
  System.out.print("Blimey! No Plunder!!");
  }
}
}
