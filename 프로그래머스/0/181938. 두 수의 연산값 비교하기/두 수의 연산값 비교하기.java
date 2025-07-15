class Solution {
    public int solution(int a, int b) {
        String s = String.valueOf(a) + String.valueOf(b);
        int sum = Integer.parseInt(s);
        int product = 2 * a * b;
        
        return Math.max(sum, product);
    }
}