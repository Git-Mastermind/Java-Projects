
import java.util.ArrayList;
public class Income {
    int checkCode = 67;
    Balance balance = new Balance();
    int totalBalance = 0;
    public int addIncome(int amount, String method) {
        if (!method.equals("check")) {
            this.changeBalance(amount);
            return 200;
            
        }
        else {
            Check check = new Check();
            check.addCheck(amount);
            return checkCode;
            
        }
    }

    public void changeBalance(int amount) {
        totalBalance += amount;
    }

    public int returnBalance() {
        return totalBalance;
    }

    
}
