package PaymentManagement;
class Merchant {
    public void receivePaymentProcessorName(int nameID) {
        if (nameID == 1) {
            paymentProcessorName.equals("stripe");
        }
    }
    String name;
    MerchantBankDetails bankDetails;
    String paymentProcessorName;

    public Merchant(String name, MerchantBankDetails bankDetails) {
        this.name = name;
        this.bankDetails = bankDetails;
        
    }

    public void receivePayment(String customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        PaymentProcessor paymentProcessor = new PaymentProcessor(paymentProcessorName);
        paymentProcessor.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
    }

    public void getAuthorizationCode(String authorizationCode) {
        
    }


}
