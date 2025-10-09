package PaymentManagement;
public class CardNetwork {
    String name;
    IssuerBank chase = new IssuerBank("Chase");
    IssuerBank bankOfAmerica = new IssuerBank("Bank Of America");
    IssuerBank wellsFargo = new IssuerBank("Wells Fargo");
    IssuerBank capitalOne = new IssuerBank("Capital One");

    public CardNetwork(String name) {
        this.name = name;
    }

    public void processPayment(String customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        if (customerCardNumber.startsWith("4")) {
            IssuerBank visa = new IssuerBank("visa");
            String authorizationCode = visa.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        else if (customerCardNumber.substring(0, 1).equals("34") || customerCardNumber.substring(0,1).equals("37")) {
            IssuerBank americanExpress = new IssuerBank("american express");
            String authorizationCode = americanExpress.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        else if (customerCardNumber.substring(0, 5).equals("407372")) {
            IssuerBank wellsFargo = new IssuerBank("wells fargo");
            String authorizationCode = wellsFargo.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        else if (customerCardNumber.substring(0, 7).equals("22212720") || customerCardNumber.substring(0, 3).equals("5155")) {
            IssuerBank mastercard = new IssuerBank("mastercard");
            String authorizationCode = mastercard.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        else if (customerCardNumber.substring(0, 5).equals("403075")) {
            IssuerBank chase = new IssuerBank("chase");
            String authorizationCode = chase.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
        else {
            IssuerBank happyBankOfDoughnutsAndPiggies = new IssuerBank("Happy Bank of Doughnuts and Piggies");
            String authorizationCode = happyBankOfDoughnutsAndPiggies.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
        }
    }
}
    

