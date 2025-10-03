import java.util.Scanner;

public class Arithmetic_Expressions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine()); 

        for (int i = 0; i < N; i++) {
            String line = sc.nextLine().trim();  
            String[] parts = line.split(" ");

            double num1 = Double.parseDouble(parts[1]);
            String ch = parts[2];
            double num2 = Double.parseDouble(parts[3]);
            double result = 0.0;

            if (ch.equals("+")){
                result = num1 + num2;
            } else if (ch.equals("-")) {
                result = num1 - num2;
            } else if (ch.equals("*")) {
                result = num1 * num2;
            } else if (ch.equals("/")) {
                result = num1 / num2;
            }
            // Print the result with exactly 6 decimal places followed by a newline
            System.out.printf("%.6f\n", result);
        }
    }
}
