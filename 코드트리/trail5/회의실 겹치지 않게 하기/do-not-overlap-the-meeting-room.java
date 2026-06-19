import java.io.*;
import java.util.*;

public class Main {
    
    static class Meeting implements Comparable<Meeting> {
        int start;
        int end;

        public Meeting(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Meeting o) {
            if (this.end != o.end) {
                return Integer.compare(this.end, o.end);
            }
            return Integer.compare(this.start, o.start);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        
        int N = Integer.parseInt(line.trim());
        Meeting[] meetings = new Meeting[N];
        
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            meetings[i] = new Meeting(start, end);
        }
        
        Arrays.sort(meetings);
        
        int acceptedCount = 0;
        int lastEndTime = -1;
        
        for (Meeting meeting : meetings) {
            if (meeting.start >= lastEndTime) {
                acceptedCount++;
                lastEndTime = meeting.end;
            }
        }
        
        System.out.println(N - acceptedCount);
    }
}