public class Task2{
  public static double circleArea(int r1){
    double area=Math.PI*r1*r1;
    return area;
  }
  public static double sphereVolume(int r2){
    double volume=(4.0/3.0)*Math.PI*(r2*r2*r2);
    return volume;
  }
  public static void findSpace(int d,String s){
    int r=d/2;
    if (s=="circle"){
      System.out.println(circleArea(r));
    }
    else if (s=="sphere"){
      System.out.println(sphereVolume(r));
    }
    else{
      System.out.println("Wrong Parameter");
    }
  }
  
  public static void main(String[]args){
   double area = circleArea(5);
   System.out.println(area);
   double volume = sphereVolume(5);
   System.out.println(volume);
   findSpace(10,"circle");  
   findSpace(5,"sphere"); 
   findSpace(10,"square");
  }
}
