import java.util.ArrayList;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;

public class KdTree {
	
	private Node root;
	private int size;
	private Point2D nearest;
	private double minDist;
    
	private static class Node {
		private final Point2D p;
		private final RectHV rect;
		private Node lb, rt;
		private final boolean vertical;
		
		public Node(Point2D p, boolean vertical, RectHV rect) {
			this.p = p;
			this.vertical = vertical;
			this.rect = rect;
		}
	}
    
	public KdTree() {
		size = 0;
	}
	
	public boolean isEmpty() {
		return root == null;
	}
	
	public int size() {
		return size;
	}
	
	public void insert(Point2D p) {
		if (p == null) throw new IllegalArgumentException();
		
		root = insert(root, p, true, 0, 0, 1, 1);
	}
	
	private Node insert(Node x, Point2D p, boolean vertical, double xmin, 
	    double ymin, double xmax, double ymax) {
		if (x == null) {
			size++;
			return new Node(p, vertical, new RectHV(xmin, ymin, xmax, ymax));
		}
		if (p.equals(x.p)) return x;
		
		if (x.vertical) {
			if (p.x() < x.p.x()) x.lb = insert(x.lb, p, false, xmin, ymin, 
				x.p.x(), ymax);
			else x.rt = insert(x.rt, p, false, x.p.x(), ymin, xmax, ymax);
		}
		else {
			if (p.y() < x.p.y()) x.lb = insert(x.lb, p, true, xmin, ymin, xmax, 
				x.p.y());
			else x.rt = insert(x.rt, p, true, xmin, x.p.y(), xmax, ymax);
		}
		
		return x;
	}
	
	public boolean contains(Point2D p) {
		if (p == null) throw new IllegalArgumentException();

		Node x = root;
		while (x != null) {
			if (p.equals(x.p)) return true;
			
			if (x.vertical) {
			    if (p.x() < x.p.x()) x = x.lb;
			    else x = x.rt; 
			}
			else {
				if (p.y() < x.p.y()) x = x.lb;
				else x = x.rt;
			}
		}
		
		return false;
	}
	
	public void draw() {
		draw(root);
	}
	
	private void draw(Node x) {
		if (x == null) return;
		
		StdDraw.setPenColor(StdDraw.BLACK);
		StdDraw.setPenRadius(0.01);
		x.p.draw();
		
		StdDraw.setPenRadius();
		if (x.vertical)  {
			StdDraw.setPenColor(StdDraw.RED);
			StdDraw.line(x.p.x(), x.rect.ymin(), x.p.x(), x.rect.ymax());
		}
		else {
			StdDraw.setPenColor(StdDraw.BLUE);
			StdDraw.line(x.rect.xmin(), x.p.y(), x.rect.xmax(), x.p.y());
		}
		
	    draw(x.lb);
	    draw(x.rt);
	}
	
	public Iterable<Point2D> range(RectHV rect) {
		if (rect == null) throw new java.lang.IllegalArgumentException();
		
		ArrayList<Point2D> inRange = new ArrayList<Point2D>();
		range(root, rect, inRange);
		
		return inRange;
	}
	
	private void range(Node x, RectHV r, ArrayList<Point2D> list) {
		if (x == null) return;
		if (!r.intersects(x.rect)) return; // Pruning rule.
		
		if (r.contains(x.p)) list.add(x.p);
		
		range(x.lb, r, list);
		range(x.rt, r, list);
	}
	
	public Point2D nearest(Point2D p) {
		if (p == null) throw new IllegalArgumentException();
		
		nearest = null;
		minDist = Double.POSITIVE_INFINITY;
		nearest(root, p);
		
		return nearest;
	}
	
	private void nearest(Node x, Point2D p) {
		if (x == null) return;
		if (x.rect.distanceTo(p) > minDist) return; // Pruning rule.
		
		if (p.distanceTo(x.p) < minDist) {
			nearest = x.p;
			minDist = p.distanceTo(x.p);
		}
		
		if ((x.vertical && p.x() < x.p.x()) ||
		    (!x.vertical && p.y() < x.p.y())) {
			nearest(x.lb, p);
			nearest(x.rt, p);
		}
		else {
			nearest(x.rt, p);
			nearest(x.lb, p);
		}
	}
	
//	public static void main(String[] args) {
//        
//	}
}
