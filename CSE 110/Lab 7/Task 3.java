public class Task3{
  public static boolean isTriangle(int s1,int s2,int s3){
    if (((s1+s2)>s3) && ((s1+s3)>s2) && ((s2+s3)>s1)){
     return true;
    }
    else{
     return false;
    }
  }  
  public static void triArea(int a,int b,int c){
    double s=(a+b+c)/2.0;
    if (isTriangle(a,b,c)){
     double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
     System.out.println(area);
    }
    else{
      System.out.println("Can’t form triangle");
    }
   }
  public static void main(String[]args){
   triArea(3,2,1);
   triArea(7,5,10);
  }
}
