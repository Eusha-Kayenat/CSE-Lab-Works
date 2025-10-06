public class Task3 {
    public static Node idGenerator(Node head1, Node head2, Node head3) {
        
       Node prev = null;
       Node current = head1;
        while (current != null) {
         Node nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }
        return prev;
    }
