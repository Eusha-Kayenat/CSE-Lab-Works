public class Task5 {
    public static int sumDist(Node head, Integer[] distArr) {
      Node h=head;
      int sum=0;
      
      for (int i=0;i<distArr.length;i++){
        int temp=distArr[i];
        h=head;
        for(int j=0;j<temp && h!=null;j++){
        h=h.next;
        }
        if (h!=null) {
        sum+=(int)h.elem;
      }
     }
      return sum;
    }
