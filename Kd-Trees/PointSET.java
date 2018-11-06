import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.SET;
import edu.princeton.cs.algs4.StdDraw;
import java.util.ArrayList;

public class PointSET {
    
	private final SET<Point2D> points;
	
	public PointSET() {
	    points = new SET<Point2D>();	
	}
	
	public boolean isEmpty() {
		return points.isEmpty();
	}
	
	public int size() {
		return points.size();
	}
	
	public void insert(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		
		points.add(p);
	}
	
	public boolean contains(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		
		return points.contains(p);
	}
	
	public void draw() {
		StdDraw.setPenRadius(0.01);
		StdDraw.setPenColor(StdDraw.BLACK);
		
		for (Point2D p : points) {
			p.draw();
		}
	}
	
	public Iterable<Point2D> range(RectHV rect) {
		if (rect == null) throw new java.lang.IllegalArgumentException();
		
		ArrayList<Point2D> inRange = new ArrayList<Point2D>();
		for (Point2D p : points) {
			if (p.x() >= rect.xmin() && p.x() <= rect.xmax() &&
				p.y() >= rect.ymin() && p.y() <= rect.ymax()) {
				inRange.add(p);
			}
		}
		
		return inRange;
	}
	
	public Point2D nearest(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		if (points.isEmpty()) return null;
		
		double minDist = 2;
		Point2D nearest = new Point2D(-1, -1);
		for (Point2D t : points) {
			if (p.distanceTo(t) < minDist) {
				nearest = t;
				minDist = p.distanceTo(t);
			}
		}
		
		return nearest;
	}
	
//	public static void main(String[] args) {
//      
//	}
}