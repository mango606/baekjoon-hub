import java.io.*;
import java.util.*;

public class Main {
    
    static class BracketString implements Comparable<BracketString> {
        long openCount;     // (의 개수
        long closedCount;   // )의 개수
        long internalScore;

        public BracketString(String str) {
            long currentOpen = 0;
            long score = 0;
            
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if (c == '(') {
                    currentOpen++;
                } else if (c == ')') {
                    score += currentOpen;
                    closedCount++;
                }
            }
            
            this.openCount = currentOpen;
            this.internalScore = score;
        }

        @Override
        public int compareTo(BracketString o) {
            long val1 = this.openCount * o.closedCount;
            long val2 = o.openCount * this.closedCount;
            
            return Long.compare(val2, val1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        
        int N = Integer.parseInt(line.trim());
        List<BracketString> list = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            list.add(new BracketString(br.readLine().trim()));
        }
        
        Collections.sort(list);
        
        long totalScore = 0;
        long accumulatedOpen = 0;
        
        for (BracketString bs : list) {
            totalScore += bs.internalScore;
            
            totalScore += accumulatedOpen * bs.closedCount;
            
            accumulatedOpen += bs.openCount;
        }
        
        System.out.println(totalScore);
    }
}