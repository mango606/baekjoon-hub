import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String str = st.nextToken();
        int n = Integer.parseInt(st.nextToken());

        System.out.println(str.repeat(n));
    }
}