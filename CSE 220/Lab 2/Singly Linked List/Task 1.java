public class Task1{
  public static Node alternateMerge( Node head1, Node head2 ){
      Node h1 = head1;
      Node h2 = head2;
      if (h1 == null){ 
        return h2;
      }
      if (h2 == null){
        return h1;
      }
      while (h1!=null && h2!=null){
            Node temp1 = h1.next;
            Node temp2 = h2.next;
            h1.next=h2;
            if (temp1 == null){ 
              break;
            }
            else{
            h2.next = temp1;
            h1 = temp1;
            h2 = temp2;
           }
          }
 
         return head1;
  }
