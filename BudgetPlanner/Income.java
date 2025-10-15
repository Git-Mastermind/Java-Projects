package BudgetPlanner;
import java.util.ArrayList;
public class Income {
    int totalBalance = 0;
    int checkCode = 67;
    public int addIncome(int amount, String method) {
        if (!method.equals("check")) {
            totalBalance += amount;
            Balance balance = new Balance();
            balance.changeBalance(amount);
            return totalBalance;
            
        }
        else {
            Check check = new Check();
            check.addCheck(amount);
            return checkCode;
        }
    }

    
}
