import java.util.Scanner;
public class Task6{
  public static void main (String [] args){
    Scanner sc=new Scanner (System.in);
    String st=sc.nextLine();
    int start=0;
    int end=st.length()-1;
    int length=st.length()-1;
    for (int i=length;i>=0;i--){
       char ch=st.charAt(i);
       if (ch==' '){
        start=i+1; 
        for(int j=start;j<=end;j++){
          char ch2=st.charAt(j);
          System.out.print(ch2 );
    }
        System.out.print(" " );
        end=i-1;
  }
}
    for(int i=0;i<=end;i++){
      char ch3=st.charAt(i);
       System.out.print(ch3 );
    }
  }
}
