import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {

        int basicTime = fees[0];   // 기본 시간
        int basicFee = fees[1];    // 기본 요금
        int unitTime = fees[2];    // 단위 시간
        int unitFee = fees[3];     // 단위 요금

        Map<String, Integer> inTime = new HashMap<>();

        Map<String, Integer> totalTime = new HashMap<>();

        for (String record : records) {
            String[] parts = record.split(" ");
            String timeStr = parts[0];
            String car = parts[1];
            String type = parts[2];

            int time = toMinute(timeStr);

            if (type.equals("IN")) {
                inTime.put(car, time);
            } else {
                int start = inTime.get(car);
                int duration = time - start;

                totalTime.put(car, totalTime.getOrDefault(car, 0) + duration);
                inTime.remove(car);
            }
        }

        for (String car : inTime.keySet()) {
            int start = inTime.get(car);
            int duration = 1439 - start;
            totalTime.put(car, totalTime.getOrDefault(car, 0) + duration);
        }

        List<String> cars = new ArrayList<>(totalTime.keySet());
        Collections.sort(cars);

        int[] answer = new int[cars.size()];
        for (int i = 0; i < cars.size(); i++) {
            int time = totalTime.get(cars.get(i));
            answer[i] = calcFee(time, basicTime, basicFee, unitTime, unitFee);
        }

        return answer;
    }

    private int toMinute(String time) {
        String[] t = time.split(":");
        int h = Integer.parseInt(t[0]);
        int m = Integer.parseInt(t[1]);
        return h * 60 + m;
    }

    private int calcFee(int time, int basicTime, int basicFee, int unitTime, int unitFee) {
        if (time <= basicTime) {
            return basicFee;
        }

        int extra = time - basicTime;
        int units = (extra + unitTime - 1) / unitTime;
        return basicFee + units * unitFee;
    }
}