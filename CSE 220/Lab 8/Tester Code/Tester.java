public class TesterCode{
 public static void main(String[] args) {
    MinHeap minHeap = new MinHeap(10);

    Object[][] operations = {
        {"insert", 30},
        {"insert", 20},
        {"insert", 40},
        {"insert", 10},
        {"insert", 60},
        {"delete"},
        {"insert", 5},
        {"delete"},
        {"sort"}
    };

    for (int i = 0; i < operations.length; i++) {
        Object[] operation = operations[i];
        String opType = operation[0].toString();
    
        if (opType.equals("insert")) {
            int val = (int) operation[1];
            minHeap.Insert(val);
            System.out.print("Inserted " + val + ": ");
            minHeap.printHeap();
        } else if (opType.equals("delete")) {
            Integer minVal = minHeap.extractMin();
            System.out.print("Deleted min value " + minVal + ": ");
            minHeap.printHeap();
        } else if (opType.equals("sort")) {
            minHeap.sort();
            System.out.print("Built min heap: ");
            minHeap.printHeap();
        } else {
            System.out.println("Unknown operation!");
        }
    }
  MaxHeap maxHeap = new MaxHeap(10);

        Object[][] Moperations = {
            {"insert", 10},
            {"insert", 20},
            {"insert", 5},
            {"insert", 30},
            {"insert", 60},
            {"delete"},
            {"insert", 25},
            {"delete"},
            {"sort"}
        };

        for (int i = 0; i < Moperations.length; i++) {
            Object[] operation = Moperations[i];
            String opType = operation[0].toString();

            if (opType.equals("insert")) {
                int value = (int) operation[1];
                maxHeap.Insert(value);
                System.out.print("Inserted " + value + ": ");
                maxHeap.printHeap();
            } else if (opType.equals("delete")) {
                Integer maxVal = maxHeap.extractMax();
                System.out.print("Deleted max value " + maxVal + ": ");
                maxHeap.printHeap();
            } else if (opType.equals("sort")) {
                maxHeap.sort();
                System.out.print("Built max heap: ");
                maxHeap.printHeap();
            } else {
                System.out.println("Unknown operation!");
            }
        }
        //Driver code for task 3
        int mach = 4;
        Integer [] n = {2,4,7,1,6};
        Task3.Extractor(n,mach);
    }
}
