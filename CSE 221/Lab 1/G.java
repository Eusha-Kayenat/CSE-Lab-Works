import java.util.*;

public class StudentSorter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        List<Integer> validID = new ArrayList<>();
        List<Integer> validMark = new ArrayList<>();
        List<Student> student = new ArrayList<>();

        String[] idInput = sc.nextLine().split(" ");
        String[] markInput = sc.nextLine().split(" ");

        for (String id : idInput) {
            validID.add(Integer.parseInt(id));
        }

        for (String mark : markInput) {
            validMark.add(Integer.parseInt(mark));
        }

        for (int i = 0; i < n; i++) {
            student.add(new Student(validID.get(i), validMark.get(i), i));
        }

        List<Student> sortedStudent = new ArrayList<>(student);
        Collections.sort(sortedStudent);

        int[] loc = new int[n];
        for (int i = 0; i < n; i++) {
            loc[sortedStudent.get(i).index] = i;
        }

        boolean[] track = new boolean[n];
        int swap = 0;

        for (int i = 0; i < n; i++) {
            if (track[i] || loc[i] == i)
                continue;

            int cycleSize = 0;
            int j = i;
            while (!track[j]) {
                track[j] = true;
                j = loc[j];
                cycleSize++;
            }

            if (cycleSize > 1) {
                swap += (cycleSize - 1);
            }
        }

        System.out.println("Minimum swaps: " + swap);
        for (Student s : sortedStudent) {
            System.out.println("ID: " + s.id + " Mark: " + s.mark);
        }

        sc.close();
    }

    static class Student implements Comparable<Student> {
        int id;
        int mark;
        int index;

        public Student(int id, int mark, int index) {
            this.id = id;
            this.mark = mark;
            this.index = index;
        }

        @Override
        public int compareTo(Student other) {
            if (this.mark != other.mark) {
                return Integer.compare(other.mark, this.mark); 
            } else {
                return Integer.compare(this.id, other.id); 
            }
        }
    }
}
