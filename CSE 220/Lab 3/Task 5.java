class Task5{
 public static void playGame( Integer[][] arena ){
        int row = arena.length;
        int col = arena[0].length;
        int points = 0;
        for (int i = 0; i < row; i++) {
          for (int j = 0; j < col; j++) {
             if (arena[i][j] % 50 == 0 && arena[i][j] > 0){
                int count = 0;
                if (i > 0 && arena[i - 1][j] == 2){
                    count++;
                 }
 
                 if (j < col - 1 && arena[i][j + 1] == 2){
                    count++;
                }
                 if (i < row-1 && arena[i + 1][j] == 2){ 
                      count++;
                 }
                 if (j > 0 && arena[i][j - 1] == 2){
                      count++;
                 }
                 points += count*2;
                }
          }
        }
        if (points>=10){
        System.out.println("Points Gained: " + points + ". " +"Your team has survived the game.");
        }
        else{
        System.out.println("Points Gained: " + points + ". " +"Your team is out.");
        }
 }
