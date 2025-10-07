public class Task3 {
        public static Integer sumTree( BTNode root ){
            return modTree(root, 0);
        }
        private static Integer modTree(BTNode root,int level){
            if(root==null || root.elem==null){
                return 0;
            }
            Integer val =(Integer)root.elem;
            int sum=0;
            if(level<=0){
               sum+=val;
            }
            else{
                sum+=(val%level);
            }
            sum+=modTree(root.left,level+1);
            sum+=modTree(root.right,level+1);
            return sum;
        }

}
