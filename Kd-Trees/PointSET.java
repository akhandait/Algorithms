import java.util.TreeSet;
import edu.princeton.cs.algs4.*;
import java.util.ArrayList;

public class PointSET {
	private TreeSet<Point2D> tset;
	
	public PointSET() {
		tset = new TreeSet<Point2D>();
	}

	public boolean isEmpty() {
		return tset.isEmpty();
	}
	
	public int size() {
		return tset.size();
	}
	
	public void insert(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		tset.add(p);
	}
	
	public boolean contains(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		return tset.contains(p);
	}
	
	public void draw() {
		StdDraw.setPenRadius(0.015);
        StdDraw.setPenColor(StdDraw.BLACK);
        
		for (Point2D p : tset) {
			StdDraw.point(p.x(), p.y());
		}
	}
	
	public Iterable<Point2D> range(RectHV rect) {
		if (rect == null) throw new java.lang.IllegalArgumentException();
		
		ArrayList<Point2D> list = new ArrayList<Point2D>();
		
		for (Point2D p : tset) {
			if (rect.contains(p)) list.add(p);
		}
		return list;
	}
	
	public Point2D nearest(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		
		Point2D clsofar = null;
		double minsofar = 0;
		
		for (Point2D P : tset) {
			if (clsofar == null) {
				minsofar = p.distanceTo(P);
				clsofar = P;
			}
			if (P.distanceTo(p) < minsofar) {
				minsofar = p.distanceTo(P);
				clsofar = P;
			}
		}
		
		return clsofar;
	}
	
    public static void main(String[] args) {
    	PointSET ps = new PointSET();
    	ps.insert(new Point2D(0.5, 0.7));
    	ps.insert(new Point2D(0.2, 0.2));
    	ps.insert(new Point2D(0.3, 0.3));
    	Point2D q = new Point2D(0.5, 0.5);
    	Point2D w = ps.nearest(q);		
    	StdDraw.setPenRadius(0.015);
    	StdDraw.setPenColor(StdDraw.BLACK);
    	StdDraw.point(w.x(), w.y());
    }
}
