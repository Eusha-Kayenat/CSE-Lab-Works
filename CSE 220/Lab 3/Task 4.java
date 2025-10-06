class Task4{
 public static Integer[][] compressMatrix( Integer[][] matrix ){
   int row_num = matrix.length;
   int colum_num = matrix[0].length;
   int rows = row_num / 2;
   int columns= colum_num / 2;
   Integer[][] array = new Integer[rows][columns];

   for (int i=0; i<rows ; i++){
     for (int j=0; j<columns;j++) {
       array[i][j] = matrix[2*i][2*j] + matrix[2 * i][2 * j + 1] +matrix[2* i + 1][2 * j] + matrix[2 * i + 1][2 * j + 1];
       }
     }
     return array;
    }
