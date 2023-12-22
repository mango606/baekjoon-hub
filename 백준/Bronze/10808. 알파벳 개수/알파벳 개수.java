import java.util.*;

public class Main
{

	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		
		String s = input.next();
		
		int[] array = new int[26]; // a~z까지 26개
		
		for(int i = 0; i < s.length(); i++)
			array[s.charAt(i) - 'a']++;
		
		for (int i : array)
			System.out.print(i + " ");
	}

}