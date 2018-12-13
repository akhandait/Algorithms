import java.util.ArrayList;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdOut;

public class Solver {

    private boolean isSolvable;
    private int moves;
    private ArrayList<Board> solution = new ArrayList<Board>();

    private class Node implements Comparable<Node> {
        private final Board board;
        private final int moves;
        private final Node previous;
        private final int manhattan; // Optimization, calculate this only once.

        public Node(Board board, int moves, Node previous) {
            this.board = board;
            this.moves = moves;
            this.previous = previous;
            this.manhattan = board.manhattan();
        }

        public int compareTo(Node b) {
            return manhattan + moves - b.manhattan - b.moves;
        }
    }

    public Solver(Board initial) {
        if (initial == null) throw new java.lang.IllegalArgumentException();

        MinPQ<Node> pq, pq2;

        pq = new MinPQ<Node>();
        pq.insert(new Node(initial, 0, null));

        pq2 = new MinPQ<Node>();
        pq2.insert(new Node(initial.twin(), 0, null));

        Node min, min2;
        Iterable<Board> neighbors, neighbors2;

        while (true) {
            min = pq.delMin();
            if (min.manhattan == 0) {
                moves = min.moves;
                isSolvable = true;
                while (min != null) {
                    solution.add(0, min.board);
                    min = min.previous;
                }
                break;
            }

            neighbors = min.board.neighbors();

            min2 = pq2.delMin();
            if (min2.manhattan == 0) {
                moves = -1;
                isSolvable = false;
                solution = null;
                break;
            }

            neighbors2 = min2.board.neighbors();

            for (Board b : neighbors) {
                if (min.previous == null || !b.equals(min.previous.board)) {
                    pq.insert(new Node(b, min.moves + 1, min));}
            }

            for (Board b : neighbors2) {
                if (min2.previous == null || !b.equals(min2.previous.board)) {
                    pq2.insert(new Node(b, min2.moves + 1, min2));}
            }
        }
    }

    public boolean isSolvable() {
        return isSolvable;
    }

    public int moves() {
        return moves;
    }

    public Iterable<Board> solution() {
        return solution;
    }

    public static void main(String[] args) {
        int[][] b = new int[3][3];
        b[0][0] = 1;
        b[0][1] = 2;
        b[0][2] = 3;
        b[1][0] = 4;
        b[1][1] = 5;
        b[1][2] = 6;
        b[2][0] = 8;
        b[2][1] = 7;
        b[2][2] = 0;

        Solver s = new Solver(new Board(b));
    }

}
