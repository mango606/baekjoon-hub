import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        
        int N = Integer.parseInt(line.trim());
        String initialStr = br.readLine().trim();
        String targetStr = br.readLine().trim();
        
        int flipCount = 0;
        boolean isDiffBlock = false;
        
        for (int i = 0; i < N; i++) {
            if (initialStr.charAt(i) != targetStr.charAt(i)) {
                if (!isDiffBlock) {
                    flipCount++;
                    isDiffBlock = true;
                }
            } 
            else {
                isDiffBlock = false;
            }
        }
        
        System.out.println(flipCount);
    }
}