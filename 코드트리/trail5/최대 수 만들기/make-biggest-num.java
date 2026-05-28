import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        String[] nums = new String[N];
        
        for (int i = 0; i < N; i++) {
            nums[i] = br.readLine();
        }
        
        Arrays.sort(nums, (a, b) -> (b + a).compareTo(a + b));
        
        if (nums[0].equals("0")) {
            System.out.println("0");
            return;
        }
        
        StringBuilder sb = new StringBuilder();
        for (String num : nums) {
            sb.append(num);
        }
        
        System.out.println(sb.toString());
    }
}