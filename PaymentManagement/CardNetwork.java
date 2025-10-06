package PaymentManagement;
public class CardNetwork {
    String cardNetworkName;
    String issuerBankName;

    public CardNetwork(String cardNetworkName, String issuerBankName) {
        this.cardNetworkName = cardNetworkName;
        this.issuerBankName = issuerBankName;
    }

    public void processPayment(long customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        IssuerBank issuerBank = new IssuerBank(issuerBankName);

        issuerBank.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
    }
    
}
