import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Scanner;

public class Planners {
    public void budgetPlanner() {
        Scanner scanner = new Scanner(System.in);
        NumberFormat currency = NumberFormat.getCurrencyInstance();

        double totalBalance = 0;
        double[] valueOfCheck = {0};
        

        while (true){
        System.out.println("💵 Budget Planner: ");
        System.out.println("    1: Add Income");
        System.out.println("    2: Add Expense");
        System.out.println("    3: Check Balance");
        System.out.println("    4: Deposit a Check");
        System.out.println("    5: Exit");

        System.out.print("Choose an option: ");
        int optionInput = scanner.nextInt();

        while (true) {
            if (optionInput == 1) {
                System.out.println("Loading page...");
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e){
                    System.out.println("Error! Sleep was interupted!");
                }

                System.out.print("Source: ");
                String incomeSource = scanner.nextLine();
                
                System.out.print("Method (ex. Wire, Check, Direct Deposit): ");
                String incomeMethod = scanner.nextLine().toLowerCase();

                System.out.print("Amount: ");
                double incomeAmount = scanner.nextDouble();
                String formattedIncomeAmount = currency.format(incomeAmount);

                if (!incomeMethod.equals("check")) {
                    totalBalance += incomeAmount;
                }

                System.out.print("Income Date: ");
                String incomeDate = scanner.next();

                if (incomeMethod.equals("check")) {
                    valueOfCheck[0] = incomeAmount;
                }

                System.out.println(formattedIncomeAmount + " from " + incomeSource + " being deposited by " + incomeMethod + " on " + incomeDate);
                System.out.print("Submit (y/n): ");
                String submittionInput = scanner.next().toLowerCase();
                
                if (submittionInput.equals("y")) {
                    System.out.println("Submitting...");
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interupted!");
                    }
                    System.out.println("Income successfully recorded!");
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interupted!");
                    }
                    break;
                }
                else if (submittionInput.equals("n")) {
                    System.out.println("Income not recorded");
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interupted!");
                    }
                    break;
                }
                

            }

            else if (optionInput == 2) {
                while (true) {
                    System.out.println("Loading page...");
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interaupted!");
                    }

                    System.out.print("Amount: ");
                    int expenseAmount = scanner.nextInt();
                    String formattedExpenseAmount = currency.format(expenseAmount);
                    totalBalance -= expenseAmount;

                    System.out.print("Category: ");
                    String expenseCategory = scanner.next();

                    System.out.print("Date: ");
                    String expenseDate = scanner.next();

                    System.out.println(formattedExpenseAmount + " spent on " + expenseCategory + " on " + expenseDate);
                    System.out.print("Submit (y/n): ");
                    String submittionInput = scanner.next().toLowerCase();

                    if (submittionInput.equals("y")) {
                        System.out.println("Submitting...");
                        try {
                            Thread.sleep(2000);
                        }
                        catch(InterruptedException e) {
                            System.out.println("Error! Sleep was interupted!");
                        }
                        System.out.println("Expense successfully recorded!");
                        try {
                            Thread.sleep(2000);
                        }
                        catch (InterruptedException e) {
                            System.out.println("Error! Sleep was interupted!");
                        }
                        break;

                    }
                    else if (submittionInput.equals("n")) {
                        System.out.println("Expense not recorded");
                        try {
                            Thread.sleep(2000);
                        }
                        catch (InterruptedException e) {
                            System.out.println("Error! Sleep was interupted!");
                        }
                        
                    }
                    else {}
                    


                }
                break;
            }

            else if (optionInput == 3) {
                System.out.println("Loading page...");
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e) {
                    System.out.println("Error! Sleep was interupted!");
                }
                System.out.println("Balance: " + currency.format(totalBalance));
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e) {
                    System.out.println("Error! Sleep was interupted!");
                }
            }

            else if (optionInput == 4) {
                System.out.println("Loading page...");
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e) {
                    System.out.println("Error! Sleep has been interupted!");
                }
                System.out.print("Would you like to deposit your check worth " + valueOfCheck[0] + " (y/n): ");
                String checkDepositInput = scanner.next();
                if (checkDepositInput.equals("y")) {
                    System.out.println("Depositing...");
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interupted!");
                    }
                    System.out.println("Check successfully Depositied!");
                    totalBalance += valueOfCheck[0];
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interupted!");
                    }

                }

            } 
            else if (optionInput == 5) {
                System.out.println("Loading page...");
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e) {
                    System.out.println("Error! Sleep was interupted!");
                }
                System.out.print("Exit (y/n)? : ");
                String exitInput = scanner.next().toLowerCase();

                if (exitInput.equals("y")) {
                    System.out.println("Goodbye!!!");
                    System.exit(0);
                    
                }
                else if (exitInput.equals("n")) {
                    System.out.println("Thanks for staying with us!");
                    try {
                        Thread.sleep(2000);
                    }
                    catch (InterruptedException e) {
                        System.out.println("Error! Sleep was interupted!");
                    }
                    break;
                } break;
            } 

            else {
                System.out.println("Invalid!");
                break;
            } scanner.close();
                break;
                    
            
            
            
            


        }
        

    }
    }

    public void taskManager() {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        ArrayList<String> tasks = new ArrayList<String>();
        ArrayList<String> importantTasks = new ArrayList<String>();
        ArrayList<String> taskCategories = new ArrayList<String>();
        while (true) {
            
            System.out.println("""
                    Task Manager
                        1: Add Task
                        2: Mark Task as Done
                        3: Remove Tasks
                        4: View Tasks
                        5: Exit
                    """);
        
        
            System.out.print("Choose an option: ");
            int optionInput = scanner.nextInt();

            if (optionInput == 1) {
                System.out.println("Loading page...");
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e) {
                    System.out.println("Error!");
                }

                System.out.print("Name: ");
                String taskName = scanner.nextLine();
                tasks.add(taskName);

                System.out.print("Category (ex. Grocery, Travel): ");
                String taskCategory = scanner.nextLine();
                taskCategories.add(taskCategory);

                System.out.print("Importance (Low, Medium, High): ");
                String taskImportance = scanner.nextLine();
                importantTasks.add(taskImportance);

                System.out.println("Logging task...");
                main.sleep();
                
                System.out.println("Task Logged!");
                main.sleep();
                
                
            }

            else if (optionInput == 2) {
                System.out.println("Loading page...");
                main.sleep();
                int numberOfTasks = tasks.size();
                if (numberOfTasks == 0) {
                    System.out.println("No tasks!");
                }
                
                else {
                    System.out.println("Which task would you like to mark as complete?");
                    for (int i = 0; i < numberOfTasks; i++) {
                        System.out.println((i + 1) + ": " + tasks.get(i));
                    }
                }
                
                
                
            }
            else if (optionInput == 3) {
                System.out.println(tasks);
            }
    
}


















    }
    }
