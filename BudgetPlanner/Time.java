

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
    public void returnToMenu(int seconds) {
        for (int i = seconds; i >= 0; i--) {
            System.out.println("Returning to Menu in " + i);
            this.sleep(1000);
        }
    }



}

