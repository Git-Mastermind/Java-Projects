package __jvcache__;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadCSV {
    public static void main(String[] args) {
        String filePath = "tasks.csv";
        String line = "";

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                System.out.println("Task: " + values[0] + "Category: " + values[1] + "Priority: " + values[2]);
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}
