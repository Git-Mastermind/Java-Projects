import java.util.Arrays;
import java.util.Date;
import java.awt.*;
import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Temp: ");
        int temperature = scanner.nextInt();
        if (temperature > 65) {
            System.out.println("It's a hot day! Drink plenty of water");
        }
    else if (temperature > 20 && temperature < 30) {
        System.out.println("It's a nice day");
    }
    else {
        System.out.println("It's cold");
    }

    

































}

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
} 

