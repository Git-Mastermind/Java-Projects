package TaskManager;
import java.util.ArrayList;
public class Tasks {
    ArrayList<String> tasks = new ArrayList<String>();
    ArrayList<String> taskCategories = new ArrayList<String>();

    public void addTask(String taskName, String category, String importance) {

        tasks.add(taskName);
        taskCategories.add(category);

    }

    public void removeTask(int taskIndex) {
        tasks.remove(taskIndex);
    }

    public StringBuilder viewTasks() {
        StringBuilder result = new StringBuilder();
        if (tasks.size() == 0) {
            return result.append("No tasks!");
        }
        else {
            for (int i = 0; i < tasks.size(); i++) {
                result.append(i + 1).append(": ").append(tasks.get(i)).append("\n");
            }
            return result;
        }
        
    }

    public void removeTasks(int taskIndex) {
        tasks.remove(taskIndex);
        tasks.contains("e");
    }
}
