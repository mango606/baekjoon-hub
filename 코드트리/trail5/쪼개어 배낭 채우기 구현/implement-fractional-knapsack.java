import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

class Jewel implements Comparable<Jewel> {
    double weight;
    double price;
    double unitPrice;

    public Jewel(double weight, double price) {
        this.weight = weight;
        this.price = price;
        this.unitPrice = price / weight;
    }

    @Override
    public int compareTo(Jewel other) {
        return Double.compare(other.unitPrice, this.unitPrice);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        double m = Double.parseDouble(st.nextToken());

        Jewel[] jewels = new Jewel[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            double weight = Double.parseDouble(st.nextToken());
            double price = Double.parseDouble(st.nextToken());
            jewels[i] = new Jewel(weight, price);
        }

        Arrays.sort(jewels);

        double totalValue = 0.0;

        for (int i = 0; i < n; i++) {
            if (m >= jewels[i].weight) {
                m -= jewels[i].weight;
                totalValue += jewels[i].price;
            } else {
                totalValue += m * jewels[i].unitPrice; 
                break;
            }
        }

        System.out.printf("%.3f\n", totalValue);
    }
}