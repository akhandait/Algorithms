import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;
//import edu.princeton.cs.algs4.QuickFindUF;

public class Percolation {

    private boolean[][] grid;
    private final int l;
    private int nofOpen;
    private WeightedQuickUnionUF wqu;
    private WeightedQuickUnionUF wqu2;
//  private QuickFindUF wqu;
//  private QuickFindUF wqu2;

    public Percolation(int n) {
        if (n <= 0) throw new IllegalArgumentException();

        grid = new boolean[n][n];
        l = n;

        if (n == 1) {
            wqu = new WeightedQuickUnionUF(n * n + 2);
//          wqu = new QuickFindUF(n * n + 2);
            return;
        }

        wqu = new WeightedQuickUnionUF(n * n + 2);
        wqu2 = new WeightedQuickUnionUF(n * n + 2);
//      wqu = new QuickFindUF(n * n + 2);
//      wqu2 = new QuickFindUF(n * n + 2);

        for (int i = 1; i < n + 1; i++) {
            wqu.union(0, i);
            wqu2.union(0, i);
            wqu.union(n * n - i + 1, n * n + 1);
        }
    }

    public void open(int row, int col) {
        if (row < 1 || row > l || col < 1 || col > l) {
            throw new IllegalArgumentException();
        }

        if (grid[row - 1][col - 1]) return;

        grid[row - 1][col - 1] = true;
        nofOpen += 1;

        if (l == 1) return;

        for (int i = row - 2; i < row + 1; i += 2) {
            try {
                if (grid[i][col - 1]) {
                    wqu.union((row - 1) * l + col, i * l + col);
                    wqu2.union((row - 1) * l + col, i * l + col);
                }
            }
            catch (IndexOutOfBoundsException e) {}
        }
        for (int i = col - 2; i < col + 1; i += 2) {
            try {
                if (grid[row - 1][i]) {
                    wqu.union((row - 1) * l + col, (row - 1) * l + i + 1);
                    wqu2.union((row - 1) * l + col, (row - 1) * l + i + 1);
                }
            }
            catch (IndexOutOfBoundsException e) {}
        }
    }

    public boolean isOpen(int row, int col) {
        if (row < 1 || row > l || col < 1 || col > l) {
            throw new IllegalArgumentException();
        }

        return grid[row - 1][col - 1];
    }

    public boolean isFull(int row, int col) {
        if (row < 1 || row > l || col < 1 || col > l) {
            throw new IllegalArgumentException();
        }

        if (l == 1) return isOpen(1, 1);

        if (isOpen(row, col)) {
            return wqu2.connected(0, (row - 1) * l + col);
        }
        else return false;
    }

    public int numberOfOpenSites() {
        return nofOpen;
    }

    public boolean percolates() {
        if (l == 1) return isOpen(1, 1);

        return wqu.connected(0, l * l + 1);
    }

    public static void main(String[] args) {
        // Percolation p = new Percolation(6);
        // p.open(3, 1);
        // p.open(1, 1);
        // p.open(2, 1);
        // StdOut.println(p.isFull(1, 1));
        // StdOut.println(p.isFull(2, 1));
        // StdOut.println(p.percolates());
    }

}
