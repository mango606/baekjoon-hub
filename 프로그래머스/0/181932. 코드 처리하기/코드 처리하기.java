class Solution {
    public String solution(String code) {
        int mode = 0;
        StringBuilder ret = new StringBuilder();

        for (int i = 0; i < code.length(); i++) {
            char currentChar = code.charAt(i); // 현재 문자

            if (currentChar == '1') {
                mode = 1 - mode;
                continue;
            }

            if (mode == 0) {
                if (i % 2 == 0) {
                    ret.append(currentChar);
                }
            } else {
                if (i % 2 != 0) {
                    ret.append(currentChar);
                }
            }
        }

        String answer = ret.toString();
        return answer.isEmpty() ? "EMPTY" : answer;
    }
}