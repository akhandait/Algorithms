import java.util.Comparator;
import edu.princeton.cs.algs4.StdDraw;

public class Point implements Comparable<Point> {
	private int x;
	private int y;
	
	private final Comparator<Point> slopeo = new byslope();
	
	private class byslope implements Comparator<Point> {
		public int compare(Point p1, Point p2) {
			if (slopeTo(p1) < slopeTo(p2)) return -1;
            if (slopeTo(p1) > slopeTo(p2)) return 1;
            return 0;
		}
	}
	
	public Point(int a, int b) {
		x = a;
		y = b;
	}

	public void draw() {
		StdDraw.point(x, y);
	}
	
	public void drawTo(Point that) {
		StdDraw.line(this.x, this.y, that.x, that.y);
	}
	
	public String toString() {
		return "(" + x + ", " + y + ")";
	}
	
	public int compareTo(Point that) {
             if (this.y < that.y) return -1;
	     if (this.y > that.y) return 1;
	     if (this.x < that.x) return -1;
	     if (this.x > that.x) return 1;
	     return 0;
	}
	
	public double slopeTo(Point that) {
		if (this.x == that.x) {
			if (this.y == that.y) return Double.NEGATIVE_INFINITY;
			return Double.POSITIVE_INFINITY;
		}
		if (this.y == that.y) return 0; //return positive zero
		return (double) (that.y - this.y)/(that.x - this.x);
	}
	
	public Comparator<Point> slopeOrder() {
		return slopeo;
	}
}
