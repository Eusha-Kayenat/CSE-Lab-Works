import java.util.Scanner;
public class Task6{
  public static double calcTax(int age,int salary){
    double tax=0;
    if ((age<18) || (salary<10000)){
     tax=0.0;
    }
    else{
      if ((salary>=10000) && (salary<=20000)){
        tax=(7.0/100.0)*salary;
      }
      else{
        tax=(14.0/100.0)*salary;
      }
    }
    return tax;
  }
  public static void calcYearlyTax(){
   Scanner sc = new Scanner(System.in);
   System.out.print("Enter your age: ");
   int age = sc.nextInt(); 
   double total=0.0;
   double tax=0.0;
   for (int i=1;i<=12;i++){
    int salary=sc.nextInt();
    tax=calcTax(age,salary);
    total+=tax;
    System.out.println("Month"+i+" tax: "+tax);
   }
    System.out.println("Total Yearly Tax: "+total);
   }
    
  public static void main(String[]args){
   double t = calcTax(16,20000);
   System.out.println(t);
   calcYearlyTax();
  }
}
