import java.util.*;

class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String prefix = my_string.substring(0, s);
        StringBuilder sb = new StringBuilder(prefix);

        sb.append(overwrite_string);

        sb.append(my_string.substring(s + overwrite_string.length()));

        return sb.toString();
    }
}