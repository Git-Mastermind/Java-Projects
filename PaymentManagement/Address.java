package PaymentManagement;

public class Address {
    int houseNumber;
    String unit;
    String street;
    String city;
    String state;
    int zipCode;

    public Address(int houseNumber, String unit, String street, String city, String state, int zipCode) {
        this.houseNumber = houseNumber;
        this.unit = unit;
        this.street = street;
        this.city = city;
        this.state = state;
        this.zipCode = zipCode;
    }
}
