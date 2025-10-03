import java.util.Scanner;
public class Task8{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter a String: ");
    String s=sc.nextLine();
    String output="";
    int counter=0;
    for(int i=0;i<s.length();i=i+1){
      char ch=s.charAt(i);
    if((ch>='a'&& ch<='z')||(ch>='A'&& ch<='Z')){
      if(counter%2==0){
        if(ch>='A' && ch<='Z'){
          ch=(char)(ch+32);
        }
      }
      else{
        if(ch>='a' && ch<='z'){
          ch=(char)(ch-32);
        }
      }
      counter=counter+1;
    }
    output=output+ch;
    }
    System.out.println(output);
  }
}
