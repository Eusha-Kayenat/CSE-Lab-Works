public class Task5 {
    public static Integer subtractSummation( BTNode root ){
        int L=sumTree(root.left,0);
        int R=sumTree(root.right,0);
        return L-R;
    }
    private static Integer sumTree(BTNode root,int sum){
       if(root==null){
        return 0;
       }
       int L=sumTree(root.left,sum);
       int R=sumTree(root.right,sum);
       sum+=(Integer)root.elem;
       sum+=L+R;
       return sum;
    }
       
}
