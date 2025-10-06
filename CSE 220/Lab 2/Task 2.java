public class Task2 {
  public static Node wordDecoder( Node head ){
   int count=0;
   Node h1=head;
   while (h1!=null){
       count++;
       h1=h1.next; 
   }
   int x=count%10;
   Node new_head=null;
   Node new_tail=null;
   Node temp=head;
   int i=0;
   while (temp!=null){
   if (i%x==0){
     Node newNode = new Node(temp.elem);
     newNode.next = new_head;
     new_head= newNode;
   }
     temp = temp.next;
     i++;
   }    
    return new_head;
   }
