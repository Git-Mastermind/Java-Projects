package PaymentManagement;
public class PaymentProcessor {
    String name;
    CardNetwork cardNetworkName;
    CardNetwork visa = new CardNetwork("visa");
    CardNetwork mastercard = new CardNetwork("mastercard");
    CardNetwork americanExpress = new CardNetwork("American Express");

    public PaymentProcessor(String name) {
        this.name = name;
    }

    public void processPayment(String customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        if (customerCardNumber.startsWith("4")) {
            CardNetwork cardNetwork = new CardNetwork("visa");
            cardNetwork.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        else if (customerCardNumber.startsWith("5") || customerCardNumber.startsWith("2")) {
            CardNetwork cardNetwork = new CardNetwork("mastercard");
            cardNetwork.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        
    }

    public void getAuthorizationCode(String authorizationCode) {
        System.out.println(authorizationCode);
        CustomerOrder customer = new CustomerOrder("Eshan Jha", 4444-4444-4444-4444, 123, "136 239th Way SE", "2027/04/05");
        customer.receivedAuthorizationCode();

    }





}
