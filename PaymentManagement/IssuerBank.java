package PaymentManagement;
public class IssuerBank {
    String name;

    public IssuerBank(String name) {
        this.name = name;
    }

    public String processPayment(String customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        return "856";
    }
}
