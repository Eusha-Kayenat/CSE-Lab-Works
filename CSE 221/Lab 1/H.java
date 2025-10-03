import java.util.*;

public class SortByNameAndTime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        List<StudentInfo> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            String[] words = line.split(" ");

            String name = words[0];
            String time = words[6];  

            String[] timeParts = time.split(":");
            int hour = Integer.parseInt(timeParts[0]);
            int minute = Integer.parseInt(timeParts[1]);
            int totalMinutes = hour * 60 + minute;

            list.add(new StudentInfo(name, totalMinutes, i, line));
        }

        Collections.sort(list);

        for (StudentInfo info : list) {
            System.out.println(info.line);
        }

        sc.close();
    }

    static class StudentInfo implements Comparable<StudentInfo> {
        String name;
        int time;  
        int index;   
        String line;   

        StudentInfo(String name, int time, int index, String line) {
            this.name = name;
            this.time = time;
            this.index = index;
            this.line = line;
        }

        @Override
        public int compareTo(StudentInfo other) {
            int nameCompare = this.name.compareTo(other.name);
            if (nameCompare != 0) {
                return nameCompare; 
            }

            return Integer.compare(other.time, this.time);
        }
    }
}
