import java.util.*;
import java.io.*;

public class Main {
    static List<Long> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if (n > 1022) {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i < 10; i++) {
            generateDecreasingNumber(i, 1);
        }

        Collections.sort(list);

        System.out.println(list.get(n));
    }

    public static void generateDecreasingNumber(long num, int depth) {
        if (depth > 10) {
            return;
        }

        list.add(num);

        for (int i = 0; i < num % 10; i++) {
            generateDecreasingNumber((num * 10) + i, depth + 1);
        }
    }
}