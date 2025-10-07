
    public class Calculator {
        Time time = new Time();

    public int add(int num1, int num2) {
        System.out.println("Calculating...");
        time.sleep(1500);
        return num1 + num2;
    }
    
    public int subtract(int num1, int num2) {
        System.out.println("Calculating...");
        time.sleep(1500);
        return num1 - num2;
    }

    public int multiply(int num1, int num2) {
        System.out.println("Calculating...");
        time.sleep(1500);
        return num1 * num2;
    }

    public double divide(double num1, double num2) {
        System.out.println("Calculating...");
        time.sleep(1500);
        return num1 / num2;
    }

    public double pow(int num1, int num2) {
        System.out.println("Calculating...");
        time.sleep(1500);
        return Math.pow(num1, num2);
    }
}
