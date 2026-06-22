import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        if (!st.hasMoreTokens()) return;
        
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        
        boolean[] isColored = new boolean[n + 1];
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < q; i++) {
            int target = Integer.parseInt(br.readLine().trim());
            
            int curr = target;
            int blockNode = 0;
            
            while (curr > 0) {
                if (isColored[curr]) {
                    blockNode = curr;
                }
                curr /= 2;
            }
            
            if (blockNode == 0) {
                isColored[target] = true;
                sb.append(0).append("\n");
            } 
            else {
                sb.append(blockNode).append("\n");
            }
        }
        
        System.out.print(sb);
    }
}