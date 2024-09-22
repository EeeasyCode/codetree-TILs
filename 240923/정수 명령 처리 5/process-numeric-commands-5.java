public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i=0; i<n; i++) {
            int oper = sc.next();

            if (oper == "size") {
                System.out.println(arr.size());
                continue;
            }

            int num = sc.nextInt();

            if (oper == "push_back") {
                arr.add(num);
                continue;
            }

            if (oper == "pop_back") {
                arr.remove(arr.size()-1);
                continue;
            }

            if (oper == "get") {
                System.out.println(arr.get(num-1));
                continue;
            }
        }

    }
}