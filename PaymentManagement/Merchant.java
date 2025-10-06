package PaymentManagement;
class Merchant {
    String name;
    MerchantBankDetails bankDetails;

    public Merchant(String name, MerchantBankDetails bankDetails) {
        this.name = name;
        this.bankDetails = bankDetails;
    }

    public void receivePayment(long customerCardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        PaymentProcessor paymentProcessor = new PaymentProcessor();
        paymentProcessor.processPayment(customerCardNumber, cvvNumber, billingAddress, expirationDate);
    }


}
