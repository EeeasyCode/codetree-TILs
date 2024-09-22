import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i=0; i<n; i++) {
            String oper = sc.next();

            if (oper.equals("size")) {
                System.out.println(arr.size());
                continue;
            }
            
            if (oper.equals("pop_back")) {
                arr.remove(arr.size()-1);
                continue;
            }

            int num = sc.nextInt();

            if (oper.equals("push_back")) {
                arr.add(num);
                continue;
            }

            if (oper.equals("get")) {
                System.out.println(arr.get(num-1));
                continue;
            }
        }

    }
}