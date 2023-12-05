class Solution {
    public int dfs(int[] numbers, int target, int depth, int sum){
        if(depth == numbers.length) {
            if(sum == target) return 1;
            else return 0;
        }
        
        // 현재 depth의 정수를 더해서 다음 depth의 dfs를 수행함.
        return dfs(numbers, target, depth+1, sum+numbers[depth]) + 
        // 현재 depth의 정수를 빼서 다음 depth의 dfs를 수행함.
        dfs(numbers, target, depth+1, sum-numbers[depth]);
    }
    
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
}