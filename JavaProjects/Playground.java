public class Playground {
    public static int countdown(int n) {
        if (n == 0) {
            return n;
        }
        else {
            return countdown(n - 1);
        }
    }
    public static void main(String[] args) {
        int result = countdown(5);
        System.out.println(result);
    } 
}
