package PaymentManagement;
abstract class Merchant {
    String name;

    abstract void callPaymentProcessor();

    abstract void sendCustomerBankDetails();

    abstract void sendMerchantBankDetails();

    abstract void sendPaymentAmount();


}
