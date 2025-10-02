public class Task19{
  public static void main (String[]args){
  int a = 8;
  int b = 3;
  int c = 5;
  int circumference  = 6*a;
  double triangle_area = 0.5*(a/2)*b;
  double total_area = (4*triangle_area);
  int rectangle_area = (a*c);
  double hexagon_area = (total_area + rectangle_area);
  System.out.println("The circumference of hexagon is: " + circumference);
  System.out.println("The total area of hexagon is: " + hexagon_area);
  }
}
