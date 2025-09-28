import java.util.Scanner;

public class Calculator {
    public int add(int num1, int num2) {
        return num1 + num2;
    }
    
    public int subtract(int num1, int num2) {
        return num1 - num2;
    }

    public int multiply(int num1, int num2) {
        return num1 * num2;
    }

    public double divide(double num1, double num2) {
        return num1 / num2;
    }

    public static void main(String[] args) {
        Calculator obj = new Calculator();
        Scanner scanner = new Scanner(System.in);
        System.out.print("(A)dd, (S)ubtract, (M)ultiply or (D)ivide?: ");
        String inputOperation = scanner.next().toLowerCase();

        
        System.out.print("Number 1: ");
        int numberOne = scanner.nextInt();

        System.out.print("Number 2: ");
        int numberTwo = scanner.nextInt();

        if (inputOperation.equals("a")) {
            System.out.println(obj.add(numberOne, numberTwo));
        }

        else if (inputOperation.equals("s")) {
            System.out.println(obj.subtract(numberOne, numberTwo));
        }

        else if (inputOperation.equals("m")) {
            System.out.println(obj.multiply(numberOne, numberTwo));
        }

        else if (inputOperation.equals("d")) {
            System.out.println(obj.divide(numberOne, numberTwo));
        }
    }
}
