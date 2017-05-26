import java.util.Iterator;
import edu.princeton.cs.algs4.*;

public class Permutation {
	public static void main(String[] args)
	{
		int n = Integer.parseInt(args[0]);
		RandomizedQueue R = new RandomizedQueue();
		for (String s : args)
		{
			try{Integer.parseInt(s);} catch(NumberFormatException e) {R.enqueue(s);}
		}
		Iterator itr = R.iterator();
		for(int i=0; i<n; i++)
		{
			StdOut.println(itr.next());
		}
	}
}
