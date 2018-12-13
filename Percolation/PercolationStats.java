import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.Stopwatch;

public class PercolationStats {

    private final int l;
    private final int nofTrials;
    private final double[] threshold;
    private final double c95 = 1.96;
    private double mean, stddev;

    public PercolationStats(int n, int trials) {
        if (trials <= 0 || n <= 0) throw new IllegalArgumentException();

        l = n;
        nofTrials = trials;
        threshold = new double[trials];
        Percolation p;
        int count, row, col;

        for (int i = 0; i < trials; i++) {
            p = new Percolation(n);
            count = 0;

            while (!p.percolates()) {
                row = StdRandom.uniform(1, n+1);
                col = StdRandom.uniform(1, n+1);
                if (!p.isOpen(row, col)) {
                    p.open(row, col);
                    count++;
                }
            }

            threshold[i] = (double) count / (l * l);
        }
    }

    public double mean() {
        if (mean == 0.0) mean = StdStats.mean(threshold);
        return mean;
    }

    public double stddev() {
        if (stddev == 0.0) stddev = StdStats.stddev(threshold);
        return stddev;
    }

    public double confidenceLo() {
        if (mean == 0.0) mean = mean();
        if (stddev == 0.0) stddev = stddev();

        return mean - (c95 * stddev / Math.sqrt(nofTrials));
    }

    public double confidenceHi() {
        if (mean == 0.0) mean = mean();
        if (stddev == 0.0) stddev = stddev();

        return mean + (c95 * stddev / Math.sqrt(nofTrials));
    }

    public static void main(String[] args) {
        // int a = Integer.parseInt(args[0]);
        // int b = Integer.parseInt(args[1]);
        // int a = 200, b = 100;
        // Stopwatch w = new Stopwatch();
        // PercolationStats ps = new PercolationStats(a, b);
        // double t = w.elapsedTime();
        // StdOut.println(t + " sec");
        // String confidence = "[" + ps.confidenceLo() + ", " + ps.confidenceHi() + "]";
        // StdOut.println("mean                    = " + ps.mean());
        // StdOut.println("stddev                  = " + ps.stddev());
        // StdOut.println("95% confidence interval = " + confidence);
    }
}
