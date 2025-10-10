package PaymentManagement;

import java.util.Scanner;

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

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MerchantBankDetails merchantBankDetails = new MerchantBankDetails("Amazon", 4444-5555-6666-7777, 456);
        String name = "Eshan Jha";
        String cardNumber = "378282246310005";
        int cvvNumber = 123;
        String billingAddress = "136 239th Way SE";
        String expirationDate = "2029-09-17";
        byte paymentProcessorSelector = 1;
        if (paymentProcessorSelector == 1) {
            PaymentProcessor stripe = new PaymentProcessor("Stripe");
        }
        else if (paymentProcessorSelector == 2) {
            PaymentProcessor pTech = new PaymentProcessor("pTech");
        }
        String paymentProcessorName = scanner.nextLine();
        PaymentProcessor paymentProcessor = new PaymentProcessor(paymentProcessorName);
        Merchant amazon = new Merchant("Amazon", merchantBankDetails);
        amazon.receivePayment(cardNumber, cvvNumber, billingAddress, expirationDate);
        
    }

    public void receivedAuthorizationCode(String authorizationCode) {
        System.out.println("Authorization Code Received! Code: " + authorizationCode);
    }
}
