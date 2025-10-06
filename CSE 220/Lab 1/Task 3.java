public class Task3 {
    public static String checkSimilar( Node building1, Node building2 ){
     Node h1=building1;
     Node h2=building2;
     while (h1!=null && h2!=null){
       if (h1.elem!=h2.elem){
         return "Not Similar";
       }
       else{
       h1 = h1.next;
       h2 = h2.next;
     }
       
    }
    return "Similar";
    }
