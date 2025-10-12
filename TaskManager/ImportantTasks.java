package TaskManager;
import java.util.ArrayList;
public class ImportantTasks {

    ArrayList<String> importantTasks = new ArrayList<String>();
    ArrayList<String> taskCategories = new ArrayList<String>();
    public void addImportantTask(String taskName, String category) {
        importantTasks.add(taskName);
        taskCategories.add(category);
    }
}
