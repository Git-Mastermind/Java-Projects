
import java.util.Scanner;


public class BudgetPlanner {
    
    
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        
        BudgetPlannerFuncs budgetPlanner = new BudgetPlannerFuncs();
       while (true) {

        System.out.println(budgetPlanner.titleScreen());
        
        System.out.print("Choose an option: ");
        int optionInput = scanner.nextInt();
        scanner.nextLine();

        if (optionInput == 1) {
            budgetPlanner.addIncome();
        }
        else if (optionInput == 2) {
            budgetPlanner.addExpense();
        }
        else if (optionInput == 3) {
            budgetPlanner.viewBalance();
        }

        else if (optionInput == 4) {
            budgetPlanner.depositCheck();
        }

        else if (optionInput == 5) {
            budgetPlanner.exit();
        }

        else {
            budgetPlanner.invalidInput();
            
        }

       }
       
      }

}
