class Task2{
    public static void mostWater( Integer[] height ){
     int x=0;
     int y = height.length-1;
     int max = 0;
     
     while (x < y){
      int h=0;
      int b=0;
      int area=0;
      if (height[x] < height[y]){
      h = height[x];
     } 
     else{
     h = height[y];
     }
     b = y-x;
     area = (h * b);
    if (area>max) {
     max= area;
    }
    
    if (height[x] < height[y]){
     x++;
    } 
    else{
     y--;
    }
   }
     System.out.print(max);
  }
