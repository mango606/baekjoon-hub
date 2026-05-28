import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    
    static class Edge {
        int to, weight, id;
        public Edge(int to, int weight, int id) {
            this.to = to;
            this.weight = weight;
            this.id = id;
        }
    }

    static class Node implements Comparable<Node> {
        int v;
        long dist;
        public Node(int v, long dist) {
            this.v = v;
            this.dist = dist;
        }
        @Override
        public int compareTo(Node o) {
            return Long.compare(this.dist, o.dist);
        }
    }

    static int N, M;
    static List<Edge>[] graph;
    static int[] parentVertex;
    static int[] parentEdgeId;
    static final long INF = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Edge(v, w, i));
            graph[v].add(new Edge(u, w, i));
        }

        parentVertex = new int[N + 1];
        parentEdgeId = new int[N + 1];
        Arrays.fill(parentVertex, -1);
        Arrays.fill(parentEdgeId, -1);

        long originalDist = dijkstra(-1, true);

        if (originalDist == INF) {
            System.out.println(0);
            return;
        }

        List<Integer> pathEdges = new ArrayList<>();
        int curr = N;
        while (curr != 1) {
            pathEdges.add(parentEdgeId[curr]);
            curr = parentVertex[curr];
        }

        int ans = 0;
        for (int skipEdgeId : pathEdges) {
            long newDist = dijkstra(skipEdgeId, false);
            if (newDist > originalDist) {
                ans++;
            }
        }

        System.out.println(ans);
    }

    static long dijkstra(int skipEdgeId, boolean savePath) {
        long[] dist = new long[N + 1];
        Arrays.fill(dist, INF);
        PriorityQueue<Node> pq = new PriorityQueue<>();

        dist[1] = 0;
        pq.offer(new Node(1, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int u = current.v;

            if (current.dist > dist[u]) continue;

            for (Edge edge : graph[u]) {
                if (edge.id == skipEdgeId) continue;

                int v = edge.to;
                long nextDist = current.dist + edge.weight;

                if (nextDist < dist[v]) {
                    dist[v] = nextDist;
                    if (savePath) {
                        parentVertex[v] = u;
                        parentEdgeId[v] = edge.id;
                    }
                    pq.offer(new Node(v, nextDist));
                }
            }
        }

        return dist[N];
    }
}