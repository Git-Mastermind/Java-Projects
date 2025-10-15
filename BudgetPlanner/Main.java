package BudgetPlanner;
import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       Time time = new Time();
       Income incomes = new Income();
       NumberFormat currency = NumberFormat.getCurrencyInstance();
       
       while (true) {
        System.out.println("""
               Budget Planner 
                    1: Add Income
                    2: Add Expense
                    3: Check Balance
                    4: Deposit a Check
                    5: Exit
               """);
        
        System.out.print("Choose an option: ");
        int optionInput = scanner.nextInt();
        scanner.nextLine();  

        if (optionInput == 1) {
            time.loadPage(2000);

            System.out.print("Amount: ");
            int incomeAmount = scanner.nextInt();
            scanner.nextLine();

            System.out.print("Method (ex. Wire, Check, Direct Deposit): ");
            String incomeMethod = scanner.nextLine().toLowerCase();

            System.out.print("Source: ");
            String incomeSource = scanner.nextLine().toLowerCase();

            System.out.print("Would you like to log this income (y/n)? ");
            String logIncomeInput = scanner.nextLine().toLowerCase();
            if (logIncomeInput.equals("y")) {
                int addIncome = incomes.addIncome(incomeAmount, incomeMethod);
                if (addIncome == 67) {
                    System.out.println("Check's can be deposited by pressing 4 in the main menu...");
                    System.out.println("Logging income...");
                    time.sleep(2000);
                    System.out.println("Income logged!");
                    time.sleep(650);
                }
                System.out.println("Logging income...");
                time.sleep(2000);
                System.out.println("Income logged!");
                time.sleep(250);
                
            }
            else {
                System.out.println("Income cancelled...");
                time.returnToMenu(5);
            }


        }
       }
       
      }

}
