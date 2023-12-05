class Solution {
  public int solution(int n, int[][] computers) {
      int answer = 0;
      boolean[] visited = new boolean[n]; // 배열을 false로 초기화.
      
      for (int i = 0; i < n; i++) {
          if (!visited[i]) {
              dfs(computers, i, visited);
              answer++;
          }
      }

      return answer;
  }

  boolean[] dfs(int[][] computers, int i, boolean[] visited) {
      visited[i] = true;

      for (int j = 0; j < computers.length; j++) {
          if (computers[i][j] == 1 && !visited[j]) {
              visited = dfs(computers, j, visited);
          }
      }
      
      return visited;
  }
}