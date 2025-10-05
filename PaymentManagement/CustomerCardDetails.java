package PaymentManagement;
abstract class CustomerCardDetails {
    String name;
    String billingAddress;
    long creditCardNumber;
    int CVVNumber;
    String expirationDate;

    abstract void sendCustomerCardDetails();
}
