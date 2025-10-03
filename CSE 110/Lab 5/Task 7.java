import java.util.Scanner;
public class Task7{
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.print("Enter the first string: ");
 String str1 = sc.nextLine();
 System.out.print("Enter the second string: ");
 String str2 = sc.nextLine();
 String str3 = "";

 for (int i=0; i<str1.length(); i++){
   char ch1 = str1.charAt(i);
   boolean check = false;
 for (int j=0; j<str2.length(); j++){
   if (ch1 == str2.charAt(j)){
   check = true;
   break; 
   }
  }

 if (!check){ 
  char new_ch1 =(char)(ch1-32);
  str3 += new_ch1;
  }
 }

  for (int i = 0; i < str2.length(); i++) {
    char ch2 = str2.charAt(i);
    boolean check = false;

  for (int j = 0; j < str1.length(); j++) {
  if (ch2==str1.charAt(j)) {
  check = true;
  break; 
  }
  }
  if (!check){ 
  char new_ch2 =(char)(ch2 - 32);
  str3 += new_ch2;
   }
  }

      
 System.out.print(str3);
    }
}
