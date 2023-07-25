#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int MAX = 2001;
const int INF = 1e9;

int T, n, m, t, s, g, h;
vector<pair<int, int>> graph[MAX];
int destination[MAX];
int dist[MAX];
bool passed[MAX];

void dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    dist[start] = 0;
    while(!pq.empty()) {
        int cost = pq.top().first;
        int current = pq.top().second;
        pq.pop();
        if(dist[current] < cost) continue;
        for(int i=0; i<graph[current].size(); i++) {
            int next = graph[current][i].first;
            int nextCost = cost + graph[current][i].second;
            if(nextCost < dist[next]) {
                dist[next] = nextCost;
                pq.push({nextCost, next});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T;
    while(T--) {
        cin >> n >> m >> t >> s >> g >> h;
        for(int i=1; i<=n; i++) {
            graph[i].clear();
            dist[i] = INF;
            passed[i] = false;
        }
        for(int i=0; i<m; i++) {
            int a, b, d;
            cin >> a >> b >> d;
            d *= 2;
            if((a == g && b == h) || (a == h && b == g)) d--;
            graph[a].push_back({b, d});
            graph[b].push_back({a, d});
        }
        for(int i=0; i<t; i++) {
            cin >> destination[i];
        }
        dijkstra(s);
        for(int i=0; i<t; i++)
            if(dist[destination[i]] % 2 == 1)
                passed[destination[i]] = true;
        sort(destination, destination+t);
        for(int i=0; i<t; i++)
            if(passed[destination[i]])
                cout << destination[i] << " ";
        cout << "\n";
    }
    return 0;
}