
public class Expenses {
    Balance balance = new Balance();
    public void addExpense(int amount) {
        balance.changeBalance(-amount); 
    }
}
