class Task2{
    public static Integer[] decryptMatrix( Integer[][] matrix ){
      
      int column = matrix[0].length;
      int[]sum = new int[column];
        
      for (int i=0; i<column ; i++) {
        for (int row =0; row<matrix.length; row++) {
                sum[i] += matrix[row][i];
            }
      }
        int length=column-1;
        Integer[] result = new Integer[length];
        for (int i =0; i < column-1; i++) {
            result[i] = sum[i+1]-sum[i];
        }
        return result;
    }
