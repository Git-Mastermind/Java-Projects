import java.text.NumberFormat;
import java.util.Scanner;

public class BudgetPlannerFuncs {
    static Payments payments = new Payments();
    static Expenses expense = new Expenses();
    static NumberFormat currency = NumberFormat.getCurrencyInstance();
    static Scanner scanner = new Scanner(System.in);
    static Time time = new Time();

    public String titleScreen() {
        return """
                Budget Planner:
                    1: Add Income
                    2: Add Expense
                    3: View Balance
                    4: Deposit a Check
                    5: Exit
                """;
    }


    public void addIncome() {
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
            int addIncome = payments.addIncome(incomeAmount, incomeMethod);
            if (addIncome == 67) {
                System.out.println("Check's can be deposited by pressing 4 in the main menu...");
                System.out.println("Logging income...");
                time.sleep(2000);
                System.out.println("Income logged!");
                time.sleep(550);
            }

            else {
                System.out.println("Logging income...");
                time.sleep(2000);
                System.out.println("Income logged!");
                time.sleep(550);
            }
            
            
        }
        else if (logIncomeInput.equals("n")) {
            System.out.println("Income cancelled...");
        }

        else {
            this.invalidInput();
        }

    }

    public void addExpense() {
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
        else if (logExpenseInput.equals("n")) {
            System.out.println("Expense cancelled...");
            
        }
        else {
            this.invalidInput();
        }
    }

    public void viewBalance() {
        time.loadPage(2000);

        int totalBalance = payments.returnBalance();
        String formattedTotalBalance = currency.format(totalBalance);
        System.out.println("Calculating Balance...");
        time.sleep(1500);

        System.out.println("Current Balance: " + formattedTotalBalance);
        time.sleep(2000);
    }

    public void depositCheck() {
        time.loadPage(2000);

        int totalCheckValue = payments.viewChecks();

        String formattedCheckValue = currency.format(totalCheckValue);

        System.out.println("Total Check Value: " + formattedCheckValue);

        System.out.print("Deposit (y/n)? ");
        String depositInput = scanner.nextLine().toLowerCase();

        if (depositInput.equals("y")) {
            payments.clearChecksValue();
            payments.changeBalance(totalCheckValue);
            System.out.println("Depositing check...");

            time.sleep(1500);

            System.out.println("Check deposited!");
            time.sleep(1000);
        }

        else if (depositInput.equals("n")) {
            System.out.println("Deposit Cancelled...");
            for (int i = 5; i > 0; i--) {
                System.out.println("Returning to menu in " + i);
                time.sleep(1000);
            }
        }

        else {
            this.invalidInput();
        }


    }

    public void exit() {
        System.out.print("Exit (y/n)? ");
        String exitInput = scanner.nextLine().toLowerCase();

        if (exitInput.equals("y")) {
            System.out.println("Goodbye!");
            System.exit(1);
        }
        else if (exitInput.equals("n")) {
            for (int i = 5; i > 0; i--) {
                System.out.println("Returning to menu in " + i);
                time.sleep(1000);
            }
        }
        else {
            this.invalidInput();
        }
    }

    public void invalidInput() {
        System.out.println("Invalid Input!");
        time.sleep(2000);
    }
}
