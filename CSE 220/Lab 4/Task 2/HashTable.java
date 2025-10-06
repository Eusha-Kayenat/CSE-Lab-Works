public class HashTable {
    private FruitNode[] ht;
    public HashTable(int size){
        this.ht = new FruitNode[size];
    }
    public void show(){
        for(int i=0; i<ht.length; i++){
            System.out.print( i+" " );
            FruitNode n = ht[i];
            while (n!=null){
                System.out.print("('"+n.fruit[0]+"', "+n.fruit[1]+") --> ");
                n = n.next;
            }
            System.out.println();
        }
    }
    private int hashFunction( String key ){
      int sum = 0;
      if(key.length()%2==0){
        for(int i=0;i<key.length();i=i+2){
          sum+=(int)key.charAt(i);
        }
      }
      else{
        for(int i=1;i<key.length();i=i+2){
          sum+=(int)key.charAt(i);
        }
      }
        int val = sum%ht.length;
        return val;
    }
    public void insert(String key, Integer value){
        FruitNode newNode = new FruitNode(key,value);
        int index = hashFunction(key);
        if(ht[index]==null){
          ht[index]=newNode;
        }
        else{
           FruitNode current = ht[index];
            while(current!=null){
              if(current.fruit[0].equals(key)){
               current.fruit[1]=value;
               return;
              }
              current=current.next;
            }
           current = ht[index];
           FruitNode prev = null;
           while(current!=null && (int)current.fruit[1]>(int)newNode.fruit[1]){
             prev = current;
             current = current.next;
           }
           if(prev==null){
           newNode.next=current;
           ht[index]=newNode;
           }
           else{
              prev.next=newNode;
             newNode.next=current;       
           }
        }
    }

}
