import java.io.*;
import java.util.*;

public class Main {
    
    static class Element implements Comparable<Element> {
        long count; // 개수
        long value; // 자연수 값
        
        public Element(long count, long value) {
            this.count = count;
            this.value = value;
        }
        
        @Override
        public int compareTo(Element other) {
            return Long.compare(this.value, other.value);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        int N = Integer.parseInt(line.trim());
        
        List<Element> list = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            long count = Long.parseLong(st.nextToken());
            long value = Long.parseLong(st.nextToken());
            list.add(new Element(count, value));
        }
        
        Collections.sort(list);
        
        int left = 0;
        int right = list.size() - 1;
        long maxSum = 0;
        
        while (left <= right) {
            Element lElem = list.get(left);
            Element rElem = list.get(right);
            
            if (left == right) {
                maxSum = Math.max(maxSum, lElem.value * 2);
                break;
            }
            
            long currentSum = lElem.value + rElem.value;
            maxSum = Math.max(maxSum, currentSum);
            
            long minCount = Math.min(lElem.count, rElem.count);
            
            lElem.count -= minCount;
            rElem.count -= minCount;
            
            if (lElem.count == 0) {
                left++;
            }
            if (rElem.count == 0) {
                right--;
            }
        }
        
        System.out.println(maxSum);
    }
}