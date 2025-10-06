package PaymentManagement;

public class CustomerOrder {
    String name;
    long cardNumber;
    int cvvNumber;
    String billingAddress;
    String expirationDate;

    public CustomerOrder(String name, long cardNumber, int cvvNumber, String billingAddress, String expirationDate) {
        this.name = name;
        this.cardNumber = cardNumber;
        this.cvvNumber = cvvNumber;
        this.billingAddress = billingAddress;
        this.expirationDate = expirationDate;
    }

    public void customerOrder() {
        MerchantBankDetails merchantBankDetails = new MerchantBankDetails("Amazon", 4444-5555-6666-7777, 456);
        String name = "Eshan Jha";
        long cardNumber = 0000-1111-2222-3333;
        int cvvNumber = 123;
        String billingAddress = "136 239th Way SE";
        String expirationDate = "2029-09-17";
        Merchant amazon = new Merchant("Amazon", merchantBankDetails);
        amazon.receivePayment(cardNumber, cvvNumber, billingAddress, expirationDate);
    }
}
