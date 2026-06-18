import java.io.*;
import java.util.*;

public class Main {
    
    static class Bomb implements Comparable<Bomb> {
        int score;
        int timeLimit;

        public Bomb(int score, int timeLimit) {
            this.score = score;
            this.timeLimit = timeLimit;
        }

        @Override
        public int compareTo(Bomb o) {
            if (this.timeLimit != o.timeLimit) {
                return Integer.compare(this.timeLimit, o.timeLimit);
            }
            return Integer.compare(o.score, this.score);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        int N = Integer.parseInt(line.trim());
        
        List<Bomb> bombs = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int score = Integer.parseInt(st.nextToken());
            int timeLimit = Integer.parseInt(st.nextToken());
            bombs.add(new Bomb(score, timeLimit));
        }
        
        Collections.sort(bombs);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (Bomb bomb : bombs) {
            pq.offer(bomb.score);
            
            if (pq.size() > bomb.timeLimit) {
                pq.poll(); 
            }
        }
        
        long totalScore = 0;
        while (!pq.isEmpty()) {
            totalScore += pq.poll();
        }
        
        System.out.println(totalScore);
    }
}