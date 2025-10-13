package TaskManager;
import java.util.ArrayList;

public class TaskID {
    ArrayList<String> taskNames = new ArrayList<String>();
    ArrayList<Integer> taskIDs = new ArrayList<>();
    


    public String returnTaskName(int taskID) {
        int indexOfTaskID = taskIDs.indexOf(taskID);
        if (indexOfTaskID != -1 && indexOfTaskID < taskIDs.size()) {
            return taskNames.get(indexOfTaskID);
        }
        else {
            return null;
        }
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

    public void classTest() {
        System.out.println(taskNames);
        System.out.println(taskIDs);
    }

    public void removeTask(int taskIndex) {
        taskIDs.remove(taskIndex);
        taskNames.remove(taskIndex);
    }

    public StringBuilder returnFormattedTaskNames() {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < taskNames.size(); i++) {
            result.append(i + 1).append(": ").append(taskNames.get(i)).append("\n");  
        }
        return result;
    }


    }

 

