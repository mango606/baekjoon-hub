import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
 
        long MOD = 1_000_000_007; 
        
        long[] dp = new long[Math.max(n + 1, 3)];
        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 7;
 
        for (int i = 3; i <= n; i++) {
            dp[i] = (3 * dp[i - 1] + dp[i - 2] - dp[i - 3]) % MOD;
            
            if (dp[i] < 0) {
                dp[i] += MOD;
            }
        }
 
        System.out.println(dp[n]);
    }
}