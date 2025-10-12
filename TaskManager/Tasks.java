package TaskManager;
import java.util.ArrayList;
public class Tasks {
    ArrayList<String> tasks = new ArrayList<String>();
    ArrayList<String> taskCategories = new ArrayList<String>();

    public void addTask(String taskName, String category, String importance) {
        if (importance.equals("h")) {
            ImportantTasks importantTask = new ImportantTasks();
            importantTask.addImportantTask(taskName, category);
        }
        else {
            tasks.add(taskName);
            taskCategories.add(category);
        }
    }

    public String removeTask(String taskName) {
        if (tasks.contains(taskName)) {
            tasks.remove(taskName);
            return "Task Removed!";
        }
        else {
            return "No Task Found!";
        }
    }

    public ArrayList<String> viewTasks() {
        return tasks;
    }
}
