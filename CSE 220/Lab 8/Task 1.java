public class MinHeap {
    private int []heap;
    private int size;

    public MinHeap(int capacity){
        heap = new int[capacity+1];
        size = 0;  
    }

    private void sink(int index) {
        int left = 2*index;
        int right = 2*index+1;
        int smallest = index;

        if (left <= size && heap[left] < heap[smallest]) {
            smallest = left;
        }

        if (right <= size && heap[right] < heap[smallest]) {
            smallest = right;
        }

        if (smallest != index) {
            int temp = heap[index];
            heap[index] = heap[smallest];
            heap[smallest] = temp;
            sink(smallest);
        }
    }
    public void swim(int idx, int key) {
        if (key > heap[idx]) {
            System.out.println("New key is larger than current key. Cannot insert.");
            return;
        }

        heap[idx] = key;
        while (idx > 1 && heap[idx/2] > heap[idx]) {
            int parentIdx = idx/2;
            int temp = heap[idx];
            heap[idx] = heap[parentIdx];
            heap[parentIdx] = temp;
            idx = parentIdx;
        }
    }
        public void Insert(int key) {
            if (size >= heap.length - 1) {
                System.out.println("No Space Left for " + key);
                return;
            }
    
            size++;
            heap[size] = Integer.MAX_VALUE;
            swim(size, key);
        }
    
        public Integer extractMin() {
            if (size < 1) {
                return null;
            }
            int minValue = heap[1];
            heap[1] = heap[size];
            size--;
            sink(1);
            return minValue;
        }

        public void sort(){
            for (int i = size / 2; i >= 1; i--) {
                sink(i);
            }
        }
        
        public void printHeap() {
            System.out.print("Heap: ");
            for (int i = 1; i <= size; i++) {
                System.out.print(heap[i] + " ");
            }
            System.out.println();
        }
}
