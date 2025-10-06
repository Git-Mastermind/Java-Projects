package PaymentManagement;
public class PaymentProcessor {
    String cardNetworkName;
    String issuerBankName;


    public PaymentProcessor(String cardNetworkString, String issuerBankName) {
        this.cardNetworkName = cardNetworkName;
        this.issuerBankName = issuerBankName;
        
    }

    public void processPayment(long customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        CardNetwork cardNetwork = new CardNetwork(cardNetworkName, issuerBankName);

        cardNetwork.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
    }

}
