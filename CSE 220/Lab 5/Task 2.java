public class Task2 {
    public static void smallestLevel( BTNode root, Integer[] levelArray, int lvl ){
        if(root==null){
            return;
        }
        if (levelArray[lvl] == null) {
            levelArray[lvl] = (Integer) root.elem;
        }
        else if((Integer)root.elem<levelArray[lvl]){
            levelArray[lvl]=(Integer)root.elem;
        }
        smallestLevel(root.left, levelArray, lvl+1);
        smallestLevel(root.right, levelArray, lvl+1);
    }
}
