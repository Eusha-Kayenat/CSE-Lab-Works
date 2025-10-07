public class Task4 {
    public static Integer mirrorSum( BSTNode root ){
        return helperF(root.left,root.right);
        }
    private static Integer helperF(BSTNode L, BSTNode R){
        if(L==null && R==null){
            return 0;
        }
        if(L==null || R==null){
            return 0;
        }
        int sum = L.elem + R.elem;
        sum+=helperF(L.left, R.right);
        sum+=helperF(L.right, R.left);
        return sum;
    }
}
