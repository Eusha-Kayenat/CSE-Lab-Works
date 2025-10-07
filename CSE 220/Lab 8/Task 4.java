public class Task4{
    public static Integer [] Maxx(Integer [] n, int m){
        MaxHeap heap = new MaxHeap();
        int [] mach = new int[m+1];
        for (int i = 0; i < mach.length; i++) {
            heap.Insert(n[i]);
        }
        int val = n.length-1;
        while(val>m){
          int max = heap.extractMax();
          for(int i=0;i<mach.length;i++){
            if(val>mach[i]){
              mach[i]=val;
              break;
            }
            val--;
          }
        }
        return mach;
    }
}
