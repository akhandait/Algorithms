import java.util.Arrays;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Queue;

public class Board {

    private final int[][] board;
    private final int n;

    public Board(int[][] blocks) {
        n = blocks.length;
        board = new int[n][];
        for (int i = 0; i < n; i++) {
            board[i] = Arrays.copyOf(blocks[i], n);
        }
    }

    public int dimension() {
        return n;
    }

    public int hamming() {
        int count = 0;

        for (int i = 0; i < n * n - 1; i++) {
            if (board[i / n][i % n] != i + 1 && board[i / n][i % n] != 0)
                count++;
        }
        if (board[n - 1][n - 1] != 0) count++;

        return count;
    }

    public int manhattan() {
        int count = 0;

        for (int i = 0; i < n * n; i++) {
            if (board[i / n][i % n] != 0) {
                count += Math.abs(i / n - (board[i / n][i % n] - 1) / n) +
                    Math.abs(i % n - (board[i / n][i % n] - 1) % n);
            }
        }

        return count;
    }

    public boolean isGoal() {
        return manhattan() == 0;
    }

    public Board twin() {
        int[][] blocks = new int[n][];
        for (int i = 0; i < n; i++) {
            blocks[i] = Arrays.copyOf(board[i], n);
        }
        int temp;

        if (blocks[0][0] != 0) {
            temp = blocks[0][0];
            if (blocks[0][1] != 0) {
                blocks[0][0] = blocks[0][1];
                blocks[0][1] = temp;
            }
            else {
                blocks[0][0] = blocks[1][0];
                blocks[1][0] = temp;
            }
        }
        else {
            temp = blocks[1][0];
            blocks[1][0] = blocks[0][1];
            blocks[0][1] = temp;
        }

        Board twin = new Board(blocks);
        return twin;
    }

    public boolean equals(Object y) {
        if (y == null || y.getClass() != this.getClass()) return false;
        if (y == this) return true;

        Board copy = (Board) y;

        return Arrays.deepEquals(this.board, copy.board);
    }

    public Iterable<Board> neighbors() {
        int blankRow = 0, blankCol = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) {
                    blankRow = i;
                    blankCol = j;
                }
            }
        }

        int[][] b;
        int temp;
        int[] lx = {0, 1, 0, -1};
        int[] ly = {-1, 0, 1, 0};

        Queue<Board> neighborsQueue = new Queue<Board>();

        for (int i = 0; i < 4; i++) {
            try {
                b = new int[n][];
                for (int j = 0; j < n; j++) {
                    b[j] = Arrays.copyOf(board[j], n);
                }

                temp = b[blankRow][blankCol];
                b[blankRow][blankCol] = b[blankRow + lx[i]][blankCol + ly[i]];
                b[blankRow + lx[i]][blankCol + ly[i]] = temp;

                neighborsQueue.enqueue(new Board(b));
            }
            catch(IndexOutOfBoundsException e) {}
        }

        return neighborsQueue;
    }

    public String toString() {
        StringBuilder stringRep = new StringBuilder();
        stringRep.append(n).append('\n');

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                stringRep.append(' ').append(board[i][j]);
            }
            stringRep.append('\n');
        }

        return stringRep.toString();
    }

    // public static void main(String[] args) {

    // }
}
