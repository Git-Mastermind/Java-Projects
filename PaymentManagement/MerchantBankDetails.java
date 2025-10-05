package PaymentManagement;
abstract class MerchantBankDetails {
    String merchantName;
    long bankAccountNumber;
    int routerNumber;

    abstract void sendMerchantBankDetails();

}
