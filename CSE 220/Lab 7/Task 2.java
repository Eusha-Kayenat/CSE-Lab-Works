public class Task2 {
    public static String findPath( BSTNode root, Integer key ){
        Integer [] temp = new Integer[50];
        Integer [] val = helperArr(root,key,temp,0); 
        return converT(val,0,key);
    }
    private static Integer[] helperArr(BSTNode root, Integer key, Integer []arr, int index){
       if(root==null){
        return null;
       }
        if(root.elem==key){
        arr[index]=key;
        return arr;
       }
       if(root.elem>key){
        arr[index]=root.elem;
        helperArr(root.left,key,arr,index+1);
       }
       if(root.elem<key){
        arr[index]=root.elem;
        helperArr(root.right,key,arr,index+1);
       }
       return arr;
    }
    private static String converT(Integer [] arr, int index,int key){
        if(arr[index]==null){
              return "No Path Found";
            }   
        if(arr[index]==key){
            return arr[index].toString();
        }
        String temp = converT(arr, index+1, key);
        if(!temp.equals("No Path Found")){
            return arr[index]+" "+temp;
        }
        return "No Path Found";
  }
}
