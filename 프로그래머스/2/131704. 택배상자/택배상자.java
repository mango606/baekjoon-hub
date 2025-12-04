import java.util.*;

class Solution {
    public int solution(int[] order) {
        Stack<Integer> stack = new Stack<>();
        int next = 1;
        int count = 0;

        for (int target : order) {

            while (next <= order.length && next < target) {
                stack.push(next);
                next++;
            }

            if (next == target) {
                count++;
                next++;
            }
            else if (!stack.isEmpty() && stack.peek() == target) {
                stack.pop();
                count++;
            }
            else {
                break;
            }
        }

        return count;
    }
}