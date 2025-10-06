public class Task4 {
  public static Boolean assembleCongaLine(Node head){
    Node h=head;
    while (h!=null && h.next!=null){
     if ((int)h.elem > (int)h.next.elem){
       return false;
     }
      h=h.next;
     }
     return true;
  }
