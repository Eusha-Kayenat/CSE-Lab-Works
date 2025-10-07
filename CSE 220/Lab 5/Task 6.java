public class Task6 {
    public static Integer levelSum( BTNode root ){
        return sumTree(root,0);
    }
        private static Integer sumTree(BTNode root,int level){
            if(root==null || root.elem==null){
                return 0;
            }
            Integer val =(Integer)root.elem;
            int sum=0;
            if(level%2==0){
               sum-=val;
            }
            else{
                sum+=val;
            }
            sum+=sumTree(root.left,level+1);
            sum+=sumTree(root.right,level+1);
            return sum;
        }
    }
