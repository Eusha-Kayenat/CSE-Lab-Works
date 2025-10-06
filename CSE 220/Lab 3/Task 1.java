class Task1{
    public static void walkZigzag( Integer[][] matrix ){
       int row = matrix.length;
       int column= matrix[0].length;
        
       for (int i=0;i<column;i++) {
         if (i%2==0){ 
           for (int j=0;j<row;j++){
             if (j%2==0){
             System.out.print(matrix[j][i] +" ");
           }
         }
       }
         else{
            for (int k=row-1; k>0; k-=2){
              if (k%2!=0){
              System.out.print(matrix[k][i] + " ");
              }
            }
        }
          System.out.println();
    }
       
    }
