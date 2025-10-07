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

    public void numberGuesser() {
        Time time = new Time();
        Scanner scanner = new Scanner(System.in);
        int randomNumber = (int) (Math.random() * 100);
        int numberOfGuesses = 7;
        while (true) {
            System.out.print("Guess (" + numberOfGuesses + "): ");
            int guess = scanner.nextInt();
            scanner.nextLine();

            if (numberOfGuesses == 1) {
                System.out.println("You ran out of guesses! The number was " + randomNumber + "!");
                System.exit(1);
            }

            if (guess == 101) {
                System.out.println("...");
                time.sleep(1500);
                System.out.println("ENTERING SECRET MODE");
                time.sleep(1500);
                System.out.println("Shh! You have entered service mode. The number is " + randomNumber);
            }
            
            else if (guess < 1 || guess > 100) {
                System.out.println("Invalid domain (1 - 100)!!!");
            }
            else {
                if (guess == randomNumber) {
                    System.out.println("You win! The number was " + randomNumber + "!");
                    System.exit(1);
                }
                else if (guess > randomNumber) {
                    System.out.println("Too high!");
                    numberOfGuesses--;
                }
                else {
                    System.out.println("Too low!");
                    numberOfGuesses--;
                }
            }
        }
        
    }
 
    
}