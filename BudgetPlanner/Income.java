package BudgetPlanner;
import java.util.ArrayList;
public class Income {
    int checkCode = 67;
    public int addIncome(int amount, String method) {
        if (!method.equals("check")) {
            
            Balance balance = new Balance();
            balance.changeBalance(amount);
            return 200;
            
        }
        else {
            Check check = new Check();
            check.addCheck(amount);
            return checkCode;
            
        }
    }

    
}
