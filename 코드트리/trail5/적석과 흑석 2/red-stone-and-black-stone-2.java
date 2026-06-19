import java.io.*;
import java.util.*;

public class Main {
    
    static class BlackStone implements Comparable<BlackStone> {
        int a; // 시작 범위
        int b; // 종료 범위

        public BlackStone(int a, int b) {
            this.a = a;
            this.b = b;
        }

        @Override
        public int compareTo(BlackStone o) {
            if (this.a != o.a) {
                return Integer.compare(this.a, o.a);
            }
            return Integer.compare(this.b, o.b);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        if (!st.hasMoreTokens()) return;
        int C = Integer.parseInt(st.nextToken()); // 빨간 돌의 수
        int N = Integer.parseInt(st.nextToken()); // 검정 돌의 수
        
        int[] redStones = new int[C];
        for (int i = 0; i < C; i++) {
            redStones[i] = Integer.parseInt(br.readLine().trim());
        }
        
        BlackStone[] blackStones = new BlackStone[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            blackStones[i] = new BlackStone(a, b);
        }
        
        Arrays.sort(redStones);
        Arrays.sort(blackStones);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        int matchCount = 0;
        int blackIdx = 0;
        
        for (int i = 0; i < C; i++) {
            int currentRed = redStones[i];
            
            while (blackIdx < N && blackStones[blackIdx].a <= currentRed) {
                pq.offer(blackStones[blackIdx].b);
                blackIdx++;
            }
            
            while (!pq.isEmpty() && pq.peek() < currentRed) {
                pq.poll();
            }
            
            if (!pq.isEmpty()) {
                pq.poll();
                matchCount++;
            }
        }
        
        System.out.println(matchCount);
    }
}