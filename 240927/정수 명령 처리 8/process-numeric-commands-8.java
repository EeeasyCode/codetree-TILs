import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> l = new LinkedList<>();

        Scanner scanner = new Scanner(System.in);
        Integer n = scanner.nextInt();

        for (int i=0; i < n; i++) {
            String oper_string = scanner.next();
            if (oper_string.equals("pop_front")) {
                Integer pop_num = l.removeFirst();
                System.out.println(pop_num);
                continue;
            }

            if (oper_string.equals("pop_back")) {
                Integer pop_num = l.removeLast();
                System.out.println(pop_num);
                continue;
            }

            if (oper_string.equals("size")) {
                Integer list_len = l.size();
                System.out.println(list_len);
                continue;
            }

            if (oper_string.equals("empty")) {
                Boolean check_empty = l.isEmpty();
                if (check_empty == false) {
                    System.out.println(0);
                } else {
                    System.out.println(1);
                }
                continue;
            }

            if (oper_string.equals("front")) {
                Integer get_num = l.get(0);
                System.out.println(get_num);
                continue;
            }

            if (oper_string.equals("back")) {
                Integer list_len = l.size();
                Integer get_num = l.get(list_len-1);
                System.out.println(get_num);
                continue;
            }
            Integer oper_num = scanner.nextInt();

            if (oper_string.equals("push_front")) {
                l.addFirst(oper_num);
                continue;
            }

            if (oper_string.equals("push_back")) {
                l.addLast(oper_num);
                continue;
            }
        }
        

    }
}