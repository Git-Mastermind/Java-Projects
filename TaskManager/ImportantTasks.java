package TaskManager;
import java.util.ArrayList;
public class ImportantTasks {

    ArrayList<String> importantTasks = new ArrayList<String>();
    ArrayList<Integer> taskIDs = new ArrayList<>();
    public void addImportantTask(String taskName, int taskID) {
        importantTasks.add(taskName);
        taskIDs.add(taskID);
    }

    public StringBuilder returnFormattedImportantTasks() {
        StringBuilder result = new StringBuilder();
        if (importantTasks.size() == 0) {
            result.append("No Important Tasks!");
            return result;
        }
        else {
        for (int i = 0; i < importantTasks.size(); i++) {
            result.append(i + 1).append(": ").append(importantTasks.get(i)).append("\n");
        }
        return result;
        }
        
    }

    public String returnImportantTaskName(int taskID) {
        int indexOfTaskID = taskIDs.indexOf(taskID);

        if (indexOfTaskID != -1 && indexOfTaskID < taskIDs.size()) {
            String taskName = importantTasks.get(indexOfTaskID);
            return taskName;
        }
        else {
            return null;
        }
    }

    public void classTest() {
        System.out.println(importantTasks);
        System.out.println(taskIDs);
    }
}
