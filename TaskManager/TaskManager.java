package TaskManager;
import java.util.Scanner;



public class TaskManager {
    static Time time = new Time();
    static Tasks task = new Tasks();
    static TaskID taskIDs = new TaskID();
    static ImportantTasks importantTasks = new ImportantTasks();
    static Scanner scanner = new Scanner(System.in);

    public void addTask() {
        time.loadPage(2000);

        System.out.print("Task Name: ");
        String taskName = scanner.nextLine();

        int taskID = taskIDs.createTaskID();

        taskIDs.addTaskName(taskName);
        

        System.out.print("Category (Ex. Grocery, Travel): ");
        String taskCategory = scanner.nextLine();

        System.out.print("Importance ((H)igh, (M)edium, (L)ow): ");
        String taskImportance = scanner.nextLine().toLowerCase();

        if (taskImportance.equals("h")) {
            int importantTaskID = taskIDs.createTaskID();
            importantTasks.addImportantTask(taskName, importantTaskID);
        }
        else {
        task.addTask(taskName, taskCategory, taskImportance);
        }
        System.out.println("Task Successfully added! Your task Id is: " + taskID);
        time.sleep(1500);
    }

    public void removeTask() {
        time.loadPage(2000);

        System.out.print("Task Id: ");
        int taskID = scanner.nextInt();
        scanner.nextLine();

        String taskName = taskIDs.returnTaskName(taskID);

        if (taskName.equals("null")) {
            System.out.println("No such task Id exists!");
        }
        else {
        System.out.println("1: " + taskName);
        time.sleep(1500);

        System.out.print("Would you like to remove this task (y/n): ");
        String removeTaskInput = scanner.nextLine().toLowerCase();

        if (removeTaskInput.equals("y")) {
            taskIDs.removeTask(0);
            task.removeTask(0);
            System.out.println("Removing task...");
            time.sleep(2000);
            System.out.println("Task removed!");
            time.sleep(2000);
        }
        else if (removeTaskInput.equals("n")) {
            System.out.println("Task will not be removed");
            System.out.println("Rebooting Visuals...");
            time.sleep(2000);

        }

        }
        
    }

    public void markTaskAsDone() {
        time.loadPage(2000);

        StringBuilder formattedTasks = taskIDs.returnFormattedTaskNames();

        System.out.println(formattedTasks);
        time.sleep(1500);

        System.out.print("Which task would you like to mark as done? ");
        int taskRemoveInput = scanner.nextInt();
        scanner.nextLine();

        int taskRemoveIndex = taskRemoveInput - 1;

        String removeTask = taskIDs.removeTask(taskRemoveIndex);

        if (removeTask.equals("Invalid Task")) {
            System.out.println("Invalid Task Number!");
            time.returnToMenu(5);
        }
        else {
        System.out.println("Marking task as done...");
        time.sleep(2000);

        System.out.println("Rebooting Visuals...");
        time.sleep(1000);
        }
        
    }

    public void viewTasks() {
        StringBuilder formattedViewTasks = task.viewTasks();
        System.out.println(formattedViewTasks);
    }

    public void viewImportantTasks() {
        time.loadPage(2000);

        StringBuilder formattedImportantTasks = importantTasks.returnFormattedImportantTasks();

        System.out.println(formattedImportantTasks);

        time.sleep(2000);

        time.returnToMenu(5);
    }

    public void exit() {
        time.loadPage(2000);

        System.out.print("Exit (y/n)? ");
        String exitInput = scanner.nextLine().toLowerCase();

        if (exitInput.equals("y")) {
            System.out.println("Goodbye!");
            scanner.close();
            System.exit(1);
        }
        else if (exitInput.equals("n")) {
            time.returnToMenu(5);
        }
    }
}

