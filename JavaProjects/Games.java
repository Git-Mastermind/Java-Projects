import java.util.Scanner;

public class Games {
    public void fizzBuzz() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Number: ");
        int number = scanner.nextInt();

        if (number % 5 == 0 && number % 3 == 0)
            System.out.println("FizzBuzz"); 
        else if (number % 5 == 0) 
            System.out.println("Fizz");
        else if (number % 3 == 0)
            System.out.println("Buzz");
        else
            System.out.println(number);
        scanner.close();
    }

    public void numeberGuesser() {
        Scanner scanner = new Scanner(System.in);
        int randomNumber = ((int) Math.random()) * 100;
        System.out.println(randomNumber);
    }
}