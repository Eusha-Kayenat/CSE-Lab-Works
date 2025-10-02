import java.util.Scanner;
public class Task11{
  public static void main (String[]args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter an input :");
    int amount = sc.nextInt();
    int customer = sc.nextInt();
    if (amount<customer){
      int x=(customer-amount);
      int note_100=x/100;
      int remaining1=(x-(100*note_100));
      int note_50=remaining1/50;
      int remaining2=remaining1-(50*note_50);
      int note_20=remaining2/20;
      int remaining3=remaining2-(20*note_20);
      int note_10=remaining3/10;
      int remaining4=remaining3-(10*note_10);
      int coin_5=remaining4/5;
      int remaining5=remaining4-(5*coin_5);
      int coin_2=remaining5/2;
      int remaining6=remaining5-(2*coin_2);
      int coin_1=remaining6/1;
     
      System.out.println("The returned amount is "+x+" taka.");
      System.out.println("100 taka note: "+note_100);
      System.out.println("50 taka note: "+note_50);
      System.out.println("20 taka note: "+note_20);
      System.out.println("10 taka note: "+note_10);
      System.out.println("5 taka coin: "+coin_5);
      System.out.println("2 taka coin: "+coin_2);
      System.out.print("1 taka coin: "+coin_1);
    } 
    else if (amount==customer){
    System.out.print("The returned amount is 0 taka.");
      
    }
    else {
     int x=(amount-customer);
     System.out.print("Please pay "+x+" taka more.");
        
      }   
    }
  }
