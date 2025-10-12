package TaskManager;
import java.util.Scanner;
import java.lang.Math;


public class Main {
    
    public static void main(String[] args) {
        Time time = new Time();
        Scanner scanner = new Scanner(System.in);
        Tasks tasks = new Tasks();

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
        time.loadPage(2000);

        System.out.print("Task Name: ");
        String taskName = scanner.nextLine();
        TaskID taskIDs = new TaskID();
        int taskID = taskIDs.createTaskID();
        taskIDs.addTaskName(taskName);
        

        System.out.print("Category (Ex. Grocery, Travel): ");
        String taskCategory = scanner.nextLine();

        System.out.print("Importance ((H)igh, (M)edium, (L)ow): ");
        String taskImportance = scanner.nextLine().toLowerCase();

        if (taskImportance.equals("h")) {
            ImportantTasks importantTask = new ImportantTasks();
            importantTask.addImportantTask(taskName, taskCategory);
            int importantTaskID = taskIDs.createTaskID();
            

        }
        else {
        tasks.addTask(taskName, taskCategory, taskImportance);
        }
        System.out.println("Task Successfully added! Your task iD is: " + taskID);
        time.sleep(1500);
        
        
    }
    else if (optionInput == 2) {
        time.loadPage(2000);

        System.out.print("Task iD: ");
        int taskID = scanner.nextInt();
        scanner.nextLine();
        TaskID taskIDs = new TaskID();
        String taskName = taskIDs.returnTaskName(taskID);
        System.out.println(taskName);

    }

    else if (optionInput == 4) {
        time.loadPage(2000);
        System.out.println(tasks.viewTasks());
        
    }
    
        }
        

        
    }
}
