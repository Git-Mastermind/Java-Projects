package TaskManager;
import java.util.Scanner;



public class TaskManager {
    static Time time = new Time();
    static Tasks task = new Tasks();
    static TaskID taskIDs = new TaskID();
    static ImportantTasks importantTasks = new ImportantTasks();
    static Scanner scanner = new Scanner(System.in);
    static TaskManagerFuncs taskManager = new TaskManagerFuncs();
    public static void main(String[] args) {
        
        
        

        while (true) {
        System.out.println(taskManager.titleScreen());
        
        System.out.print("Choose an option: ");
        int optionInput = scanner.nextInt();
        scanner.nextLine();

        if (optionInput == 1) {   
            taskManager.addTask();
        }
        else if (optionInput == 2) {
            taskManager.removeTask();
        }

        else if (optionInput == 3) {
            taskManager.markTaskAsDone();
        }

        else if (optionInput == 4) {
            taskManager.viewTasks();
            
        }
        else if (optionInput == 5) {
            taskManager.viewImportantTasks();
        }

        else if (optionInput == 6) {
            taskManager.exit();
        }
        else if (optionInput == 404) {
            TaskID classTest = new TaskID();
            classTest.classTest();
        }

        else if (optionInput == 4048) {
            importantTasks.classTest();
        }

        else {
            System.out.println("Invalid Input!");
            time.sleep(2000);
        }
        
    }
        

        
    }

}

