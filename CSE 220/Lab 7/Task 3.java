public class Task3 {
    public static Integer sumOfLeaves( BSTNode root, Integer sum ){
        if(root==null){
            return 0;
        }
        if(root.left==null && root.right==null){
            return sum+=root.elem;
        }
        return sumOfLeaves(root.left, sum) + sumOfLeaves(root.right, sum);
    }
}
