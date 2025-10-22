
public class Payments {
    int checkCode = 67;
    Balance balance = new Balance();
    int totalBalance = 0;
    Check check = new Check();
    public int addIncome(int amount, String method) {
        if (!method.equals("check")) {
            this.changeBalance(amount);
            return 200;
            
        }
        else {
            this.addCheck(amount);
            return checkCode;
            
        }
    }

    public void changeBalance(int amount) {
        balance.changeBalance(amount);
    }

    public int returnBalance() {
        return balance.returnBalance();
    }

    public void addCheck(int amount) {
        check.addCheck(amount);
    }

    public int viewChecks() {
        return check.viewChecks();
    }

    public void clearChecksValue() {
        check.clearChecksValue();
    }

    
}
