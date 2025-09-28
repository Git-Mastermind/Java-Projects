import java.text.NumberFormat;
import java.util.Scanner;

public class calculatorSelector {
    public void mortgageCalculater() {
        Scanner scanner = new Scanner(System.in);
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;
        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        float annualInterest = scanner.nextFloat();
        float rate = annualInterest / PERCENT / MONTHS_IN_YEAR;

        System.out.print("Period (Years): ");
        int period = scanner.nextInt();
        int months = period * MONTHS_IN_YEAR;

        double numeratorRate = Math.pow(1+rate, months);

        double numerator = rate * numeratorRate;
        double denominator = numeratorRate - 1;
        double result = principal * (numerator/denominator);
        NumberFormat mortgage = NumberFormat.getCurrencyInstance();
        String finalMortgage = mortgage.format(result);
        System.out.println("Monthly Mortgage: " + finalMortgage);


    }

        public void advancedMortgageCalculater() {
        Scanner scanner = new Scanner(System.in);
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT  = 100;

        int principal = 0;
        double annualInterestRate = 0;
        int periodInYears = 0;

        while (true) {
            System.out.print("Principal ($1K - $1M): ");
            principal = scanner.nextInt();
            if (principal >= 1_000 && principal <= 1_000_000) {
                break;
            }
            else {
                System.out.println("Enter a number between 1,000 and 1,000,000");
            }
        }

        while (true) {
            System.out.print("Annual Interest Rate: ");
            annualInterestRate = scanner.nextFloat();
            if (annualInterestRate <= 100) {
                break;
            }
            else {
                System.out.println("Enter a valid interest rate (1% - 100%): ");
            }
        }
        double monthlyInterest = annualInterestRate / MONTHS_IN_YEAR;
        double monthlyInterestRate = monthlyInterest / PERCENT;

        while (true) {
        System.out.print("Period (Years): ");
        periodInYears = scanner.nextInt();
        if (periodInYears >= 10 && periodInYears <= 30) {
            break;
        }
        else {
            System.out.println("Please enter a valid time frame (10 - 30 years)");
        }
        }

        double periodInMonths = periodInYears * MONTHS_IN_YEAR;

        double numerator = (principal) * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, periodInMonths));

        double denominator = Math.pow(1 + monthlyInterestRate, periodInMonths) - 1;

        double mortgageCalculation = (numerator / denominator);

        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String mortgage = currency.format(mortgageCalculation);
        System.out.println(mortgage);



        }

        public void tipCalculater() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Total: ");
        double totalBill = scanner.nextFloat();

        System.out.print("Tip (percentage): ");
        double tipPercent = scanner.nextFloat();

        double tipAmount = (totalBill * tipPercent) / 100;
        double totalAmount = totalBill + tipAmount;
        NumberFormat currency = NumberFormat.getCurrencyInstance();

        String finalBill = currency.format(totalAmount);
        System.out.println(finalBill);
    }

    public void calculator() {
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
