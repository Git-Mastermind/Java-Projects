package BudgetPlanner;
import java.text.NumberFormat;
import java.util.Scanner;

public class BudgetPlanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       Time time = new Time();
       Income income = new Income();
       Expenses expense = new Expenses();
       Balance balance = new Balance();
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

            System.out.print("Income Date: ");
            String incomeDate = scanner.nextLine();

            String formattedIncomeAmount = currency.format(incomeAmount);
            System.out.println(formattedIncomeAmount + " from " + incomeSource + " being deposited by " + incomeMethod + " on " + incomeDate);

            System.out.print("Submit (y/n)? ");
            String logIncomeInput = scanner.nextLine().toLowerCase();

            if (logIncomeInput.equals("y")) {
                int addIncome = income.addIncome(incomeAmount, incomeMethod);
                if (addIncome == 67) {
                    System.out.println("Check's can be deposited by pressing 4 in the main menu...");
                    System.out.println("Logging income...");
                    time.sleep(2000);
                    System.out.println("Income logged!");
                    time.sleep(550);
                }
                System.out.println("Logging income...");
                time.sleep(2000);
                System.out.println("Income logged!");
                time.sleep(550);
                
            }
            else {
                System.out.println("Income cancelled...");
                time.returnToMenu(5);
            }


        }
        else if (optionInput == 2) {
            time.loadPage(2000);

            System.out.print("Amount: ");
            int expenseAmount = scanner.nextInt();
            scanner.nextLine();

            System.out.print("Category (ex. Grocery): ");
            String expenseCategory = scanner.nextLine();

            System.out.print("Expense Date: ");
            String expenseDate = scanner.nextLine();

            String formattedExpenseAmount = currency.format(expenseAmount);
            System.out.println(formattedExpenseAmount + " being spent on " + expenseCategory + " on " + expenseDate);

            System.out.print("Submit (y/n)? ");
            String logExpenseInput = scanner.nextLine().toLowerCase();

            if (logExpenseInput.equals("y")) {
                expense.addExpense(expenseAmount);
                System.out.println("Logging expense...");
                time.sleep(2000);
                System.out.println("Expense logged!");
                time.sleep(550);
            }
            else {
                System.out.println("Expense cancelled...");
                time.returnToMenu(5);
            }





        }
        if (optionInput == 3) {
            time.loadPage(2000);

            int totalBalance = balance.returnBalance();
            System.out.println("Calculating Balance...");
            time.sleep(1500);

            System.out.println(totalBalance);
            time.returnToMenu(5);
        }
       }
       
      }

}
