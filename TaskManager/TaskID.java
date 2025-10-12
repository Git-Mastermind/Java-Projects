package TaskManager;
import java.util.ArrayList;

public class TaskID {
    ArrayList<String> taskNames = new ArrayList<String>();
    ArrayList<Integer> taskIDs = new ArrayList<>();


    public String returnTaskName(int taskID) {
        int indexOfTaskID = taskIDs.indexOf(taskID);
        String taskName = taskNames.get(indexOfTaskID);
        return taskName;
    }

    public int createTaskID() {
        int randomTaskID =  (int) (Math.random() * 100_000);
        if (taskIDs.contains(randomTaskID)) {
            int newTaskID =  (int) (Math.random() * 100_000);
            taskIDs.add(newTaskID);
            return newTaskID;
            
        }
        else {
            taskIDs.add(randomTaskID);
            return randomTaskID;
        }
        
    }

    public void addTaskName(String taskName) {
        taskNames.add(taskName);

    }


    }

 

