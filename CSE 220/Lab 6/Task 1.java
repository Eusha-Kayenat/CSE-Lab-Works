public class Task1 {
    public static BTNode convertMirror( BTNode root ){
        if(root==null){
            return root;
        }
        BTNode L=convertMirror(root.left);
        BTNode R=convertMirror(root.right);
        root.left=R;
        root.right=L;
        return root;
    }
}
