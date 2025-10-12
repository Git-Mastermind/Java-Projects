package TaskManager;

public class Time {
    public void sleep(int milli) {
    try {
        Thread.sleep(milli);
    }
    catch (InterruptedException e) {
        System.out.println("Error! Sleep was interupted!");
    }
}
    public void loadPage(int milli) {
        System.out.println("Loading page...");
        try {
            Thread.sleep(milli);
        }
        catch (InterruptedException e) {
            System.out.println("Error! Sleep was interrupted!");
        }
    }
}
