package PaymentManagement;
abstract class IssuerBank {
    String name;

    abstract void receiveTransactionDetails();

    abstract void sendAuthorizationCode();

    abstract void sendDeclineCode();
}
