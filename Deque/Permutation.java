import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class Permutation {

	public static void main(String[] args) {
	
		int k = Integer.parseInt(args[0]);
		RandomizedQueue<String> rq = new RandomizedQueue<String>();
		
		String item;
		
		while (!StdIn.isEmpty()) {
			item = StdIn.readString();
			rq.enqueue(item);
		}
		
		for (int i = 0; i < k; i++) {
			StdOut.println(rq.dequeue());
		}
	}

}
