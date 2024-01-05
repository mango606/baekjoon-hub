import java.util.*;

public class Main
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int[] array = new int[201];	// -100~100
		
		for (; n --> 0; array[input.nextInt() + 100]++);
		System.out.println(array[input.nextInt() + 100]);;
	}
}