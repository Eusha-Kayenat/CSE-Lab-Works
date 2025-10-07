public class Task3{
    public static Integer [] Extractor(Integer [] n, int m){
        MinHeap heap = new MinHeap();
        int [] mach = new int[m+1];
        for (int i = 0; i < mach.length; i++) {
            heap.Insert(n[i]);
        }
        int val = n[m+1];
        int mini = extractMin();
        int sum = val+mini;
        heap.Insert(sum);
        return heap;
    }
}
