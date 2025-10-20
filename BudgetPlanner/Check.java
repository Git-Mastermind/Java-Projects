

public class Check {
    int totalCheckValue = 0;
    public void addCheck(int amount) {
        totalCheckValue += amount;
    }

    public int viewChecks() {
        return totalCheckValue;
    }

    public void clearChecksValue() {
        totalCheckValue = 0;
    }
}
