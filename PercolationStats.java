import edu.princeton.cs.algs4.*;

public class PercolationStats {
	private int t1;
	private double[]c;
	private int q;
	public PercolationStats(int n, int trials) {
		if (trials <= 0 || n <= 0 ) throw new IllegalArgumentException();
		
		t1 = trials;
		q = n;
		c = new double [trials] ;
		
		for (int i = 0; i < trials; i++) {
			Percolation p = new Percolation(n);
			int w = 0;
			while (!p.percolates()) {
				int v1 = StdRandom.uniform(1, n+1);
				int v2 = StdRandom.uniform(1, n+1);
				if (!p.isOpen(v1,v2)) {
					p.open(v1, v2);
					w++;
				}
			}
			c[i] = (double) w / (q*q);
		}
	}
	
	public double mean() {
		return StdStats.mean(c);
	}

	public double stddev() {
		return StdStats.stddev(c);
	}
	
	public double confidenceLo() {
		return mean() - (1.96 * stddev() / Math.sqrt(t1));
	}
	
	public double confidenceHi() {
		return mean() + (1.96 * stddev() / Math.sqrt(t1));
	}
	
	public static void main(String[] args) {
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		PercolationStats A = new PercolationStats(a, b);
		String confidence = "[" + A.confidenceLo() + ", " + A.confidenceHi() + "]";
                StdOut.println("mean                    = " + A.mean());
                StdOut.println("stddev                  = " + A.stddev());
                StdOut.println("95% confidence interval = " + confidence);     
	}	
}

