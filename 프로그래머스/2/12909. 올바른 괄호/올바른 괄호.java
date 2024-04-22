class Solution {
    boolean solution(String s) {
        int balance = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                balance++;
            } else if (c == ')') {
                if (balance == 0) {
                    return false;
                }
                balance--;
            }
        }

        return balance == 0;
    }
}