class Task3{
    public static Integer rowRotation( Integer examWeek, String[][] matrix){
     int rows= matrix.length;
     int current_row = 0;
       for (int i = 0; i < rows; i++) {
         for (int j = 0; j < matrix[i].length; j++) {
           if (matrix[i][j].equals("AA")) {
               current_row = i;
               break;
           }
         }
       }
      int exam_row = (current_row + examWeek) % rows;
      return exam_row;  
    }
