

public class Balance {
    int totalBalance = 0;

    public void changeBalance(int changingFactor) {
        totalBalance += changingFactor;
    }

    public int returnBalance() {
        return totalBalance;
    }

}
