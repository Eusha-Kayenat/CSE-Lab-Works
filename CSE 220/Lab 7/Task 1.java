public class Task1 {
 public static Integer lowestCommonAncestor( BSTNode root, Integer x, Integer y ){
    if (root == null){
      return -1;
    }
     if (root.elem>x && root.elem>y){
       return lowestCommonAncestor(root.left,x,y);
     } 
     else if (root.elem <x && root.elem <y) {
       return lowestCommonAncestor(root.right,x,y);
     } 
     else{
       return root.elem;
     }
  }
}
