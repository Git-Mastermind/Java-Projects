package PaymentManagement;
abstract class PaymentProcessor {
    String name;

    abstract void sendCustomerBankDetails();

    abstract void receiveDetails();

    abstract void sendTransactionDetails();

    abstract void sendPaymentToMerchant();
}
