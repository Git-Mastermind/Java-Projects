import java.util.Scanner;

public class Converters {
    public void temperatureConverter() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Temperature: "); 
        double temp = scanner.nextDouble();

        System.out.print("(C)elsius, (F)areinheit or (K)elvin: ");
        String inputTempUnit = scanner.next().toLowerCase();

        if (inputTempUnit.equals("c")) {
           System.out.print("Convert into (F)areinheit or (K)elvin: ");
           String changeIntoTemp = scanner.next().toLowerCase();
           if (changeIntoTemp.equals("f")) {
            double result = ((temp * 2) * (temp / 10)) + 32;
            System.out.println(result);
           }
            
            else if (inputTempUnit.equals("k")) {
                double result = temp + 273.15;
                System.out.println(result);
        
        }
        }

        else if (inputTempUnit.equals("f")) {
            System.out.print("Convert into (C)elsius or (K)elvin: ");
            String changeIntoTemp = scanner.next().toLowerCase();
            if (changeIntoTemp.equals("c")) {
                double result = (temp - 32) / 1.8;
                System.out.println(result);
            }

            else if (changeIntoTemp.equals("k")) {
                double result = (temp - 32) * 5/9 + 273.15;
                System.out.println(result);
            }
        }

        else if (inputTempUnit.equals("k")) {
            System.out.print("Convert into (C)elsius or (F)areinheit: ");
            String changeIntoTemp = scanner.next().toLowerCase();
            if (changeIntoTemp.equals("c")) {
                double result = temp - 273.15;
                System.out.println(result);
            }

            else if (changeIntoTemp.equals("f")) {
                double result = 9/5 * (temp - 273.15) + 32;
                System.out.println(result);
            }
        }
        scanner.close();
    }
}
