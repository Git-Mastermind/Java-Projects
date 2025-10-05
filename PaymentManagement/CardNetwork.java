package PaymentManagement;
abstract class CardNetwork {
    String name;

    abstract void receiveDetails();

    abstract void sendCustomerBankDetails();

    abstract void sendTransactionDetails();
}
