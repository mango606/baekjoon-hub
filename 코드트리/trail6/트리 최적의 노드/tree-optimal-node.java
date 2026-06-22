import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] adj;
    
    static class NodeDist {
        int node;
        int dist;
        
        NodeDist(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        
        int n = Integer.parseInt(line.trim());
        
        adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj[u].add(v);
            adj[v].add(u);
        }
        
        NodeDist furthestFromStart = bfs(1, n);
        
        NodeDist furthestFromA = bfs(furthestFromStart.node, n);
        
        int diameter = furthestFromA.dist;
        
        System.out.println((diameter + 1) / 2);
    }
    
    static NodeDist bfs(int start, int n) {
        boolean[] visited = new boolean[n + 1];
        int[] dist = new int[n + 1];
        Queue<Integer> q = new LinkedList<>();
        
        q.offer(start);
        visited[start] = true;
        
        int furthestNode = start;
        int maxDist = 0;
        
        while (!q.isEmpty()) {
            int curr = q.poll();
            
            for (int next : adj[curr]) {
                if (!visited[next]) {
                    visited[next] = true;
                    dist[next] = dist[curr] + 1;
                    q.offer(next);
                    
                    if (dist[next] > maxDist) {
                        maxDist = dist[next];
                        furthestNode = next;
                    }
                }
            }
        }
        
        return new NodeDist(furthestNode, maxDist);
    }
}