import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        int N = Integer.parseInt(line.trim());
        
        int[] B = new int[N];
        boolean[] isB = new boolean[2 * N + 1];
        
        for (int i = 0; i < N; i++) {
            B[i] = Integer.parseInt(br.readLine().trim());
            isB[B[i]] = true;
        }
        
        int[] A = new int[N];
        int aIdx = 0;
        for (int i = 1; i <= 2 * N; i++) {
            if (!isB[i]) {
                A[aIdx++] = i;
            }
        }
        
        Arrays.sort(B);
        
        int score = 0;
        int bIdx = 0;
        
        for (int aIdxPtr = 0; aIdxPtr < N; aIdxPtr++) {
            if (A[aIdxPtr] > B[bIdx]) {
                score++;
                bIdx++;
            }
        }
        
        System.out.println(score);
    }
}