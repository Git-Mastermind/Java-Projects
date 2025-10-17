package TaskManager;
import java.util.Scanner;



public class TaskManager {
    static Time time = new Time();
    static Tasks task = new Tasks();
    static TaskID taskIDs = new TaskID();
    static ImportantTasks importantTasks = new ImportantTasks();
    static Scanner scanner = new Scanner(System.in);
    static TaskManagerFuncs taskManagerFuncs = new TaskManagerFuncs();
    public static void main(String[] args) {
        
        
        

        while (true) {
        System.out.println("""
            Task Manager
                1: Add Task
                2: Remove Task
                3: Mark Task as Done
                4: View Tasks
                5: View Important Tasks
                6: Exit
            """);
        
    System.out.print("Choose an option: ");
    int optionInput = scanner.nextInt();
    scanner.nextLine();

    if (optionInput == 1) {   
        taskManagerFuncs.addTask();
    }
    else if (optionInput == 2) {
        taskManagerFuncs.removeTask();
    }

    else if (optionInput == 3) {
        taskManagerFuncs.markTaskAsDone();
    }

    else if (optionInput == 4) {
        taskManagerFuncs.viewTasks();
        
    }
    else if (optionInput == 5) {
        taskManagerFuncs.viewImportantTasks();
    }

    else if (optionInput == 6) {
        taskManagerFuncs.exit();
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

