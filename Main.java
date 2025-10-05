import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public void sleep() {
        try {
            Thread.sleep(2000);
        }
        catch (InterruptedException e) {
            System.out.println("Error!");
        }
    }
    public static void main(String[] args) {
        Planners planner = new Planners();
        planner.taskManager();
}
}