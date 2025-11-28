class Solution {
    public int solution(int[][] info, int n, int m) {
        int INF = 1_000_000_000;
        int[] dp = new int[m];
        for (int i = 1; i < m; i++) dp[i] = INF;
        dp[0] = 0;

        for (int[] item : info) {
            int aTrace = item[0];
            int bTrace = item[1];

            int[] next = new int[m];
            for (int i = 0; i < m; i++) next[i] = INF;

            for (int b = 0; b < m; b++) {
                if (dp[b] == INF) continue;

                int curA = dp[b];

                // 1) A 도둑이 훔치는 경우
                int na = curA + aTrace;
                if (na < n) { // A 한계 넘으면 안 됨
                    next[b] = Math.min(next[b], na);
                }

                // 2) B 도둑이 훔치는 경우
                int nb = b + bTrace;
                if (nb < m) { // B 한계 넘으면 안 됨
                    next[nb] = Math.min(next[nb], curA);
                }
            }

            dp = next;
        }

        int answer = INF;
        for (int b = 0; b < m; b++) {
            answer = Math.min(answer, dp[b]);
        }

        return (answer >= INF ? -1 : answer);
    }
}