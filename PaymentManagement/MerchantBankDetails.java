package PaymentManagement;
public class MerchantBankDetails {
    String merchantName;
    long bankAccountNumber;
    int routerNumber;

    public MerchantBankDetails(String merchantName, long bankAccountNumber, int routerNumber) {
        this.merchantName = merchantName;
        this.bankAccountNumber = bankAccountNumber;
        this.routerNumber = routerNumber;
    }

}
