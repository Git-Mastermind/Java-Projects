import java.util.Arrays;
import java.util.Date;
import java.awt.*;
import java.nio.channels.InterruptedByTimeoutException;
import java.text.NumberFormat;
import java.util.Scanner;



public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int randomNumber = (int) (Math.random() * 101);
        int numberOfGuesses = 7;
        while (true) {
            System.out.print("Guess (" + numberOfGuesses + "): ");
            int numberGuess = scanner.nextInt();

            if (numberOfGuesses == 1) {
                System.out.println("You ran out of guesses! The number was " + randomNumber);
                break;
            }
            else if (numberGuess > 100 || numberGuess < 1) {
                System.out.println("Invalid domain (1 - 100)!");
            }

            else if (numberGuess == randomNumber) {
                System.out.println("You win! The number was " + randomNumber);
                break;
            }
            else if (numberGuess > randomNumber) {
                System.out.println("Too high!");
                numberOfGuesses--;
            }
            else if (numberGuess < randomNumber) {
                System.out.println("Too low!");
                numberOfGuesses--;
            }
        }
        scanner.close();
        

}
}
        



        
         




        
        

            


































    