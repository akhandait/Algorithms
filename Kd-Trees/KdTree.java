import java.util.ArrayList;
import edu.princeton.cs.algs4.*;

public class KdTree {
	private node root;
	private int size;
	
	private class node {
		private Point2D p;
	    private node rt, lb; //rt is right/top, lb is left/bottom
	    private boolean isHorizontal;
	    public node(Point2D l, boolean isH) {
	    	p = l;
	    	isHorizontal = isH;
	    	rt = null;
	    	lb = null;
	    }
	}
	
	public KdTree() {
		size = 0;
		root = null;
	}
	
	public boolean isEmpty() {
		return size == 0;
	}
	
	public int size() {
		return size;
	}
	
	public void insert(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		root = put(root, p, false);
	}
	
	//recursive code, check lecture 10 - slide 10
	private node put(node x, Point2D p, boolean isH) {
		if (x == null) { 
			size++;
			return new node(p, isH);
		}		
		if (x.p.x() == p.x() && x.p.y() == p.y()) {
			return x;
		}
	    if (x.isHorizontal) {
	    	if (p.y() >= x.p.y()) x.rt = put(x.rt, p, false);
	    	if (p.y() < x.p.y()) x.lb = put(x.lb, p, false); 
	    }
	    if (!x.isHorizontal) {
	    	if (p.x() >= x.p.x()) x.rt = put(x.rt, p, true);
	    	if (p.x() < x.p.x()) x.lb = put(x.lb, p, true);
	    }
	    return x;
	}
	
	public boolean contains(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		node x = root;
		while (x != null) {
			if (p.x() == x.p.x() && p.y() == x.p.y()) return true;
			
			if (x.isHorizontal) {
				if (p.y() < x.p.y()) x = x.lb;
				else if (p.y() > x.p.y()) x = x.rt; // what if equal ?
			}
			if (!x.isHorizontal) {
				if (p.x() < x.p.x()) x = x.lb;
				else if (p.x() > x.p.x()) x = x.rt; // what if equal ?
			}
		}
		return false;
	}
	 
	public void draw() {
		drawall(root, 1, 0, 1, 0);
	}
	
	private void drawall(node x, double xmax, double xmin, double ymax, double ymin) {
        if (x.isHorizontal) { 
        	StdDraw.setPenRadius(0.007);
            StdDraw.setPenColor(StdDraw.BLUE);
        	StdDraw.line(xmin, x.p.y(), xmax, x.p.y());
        }	
        else {
        	StdDraw.setPenRadius(0.007);
            StdDraw.setPenColor(StdDraw.RED);
        	StdDraw.line(x.p.x(), ymin, x.p.x(), ymax);
        }
        
        StdDraw.setPenRadius(0.015);
        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.point(x.p.x(), x.p.y());
        
        if (x.lb != null) {
        	if (x.isHorizontal) {
        		drawall(x.lb, xmax, xmin, x.p.y(), ymin);
        	}
        	else {
        		drawall(x.lb, x.p.x(), xmin, ymax, ymin);
        	}
        }	
        if (x.rt != null) {
        	if (x.isHorizontal) {
        		drawall(x.rt, xmax, xmin, ymax, x.p.y());
        	}
        	else {
        		drawall(x.rt, xmax, x.p.x(), ymax, ymin);
        	}
        }
	}
	
	public Iterable<Point2D> range(RectHV rect) {
		if (rect == null) throw new java.lang.IllegalArgumentException();
		ArrayList<Point2D>list = new ArrayList<Point2D>();
		rangecheck(root, rect, list);
		return list;
	}
	
	private void rangecheck(node x, RectHV r, ArrayList<Point2D> l) {
		if (x == null) return;
		
		if (!x.isHorizontal) {
			if (x.p.x() >= r.xmin() && x.p.x() <= r.xmax()) {
				if (x.p.y() >= r.ymin() && x.p.y() <= r.ymax()) l.add(x.p);
				rangecheck(x.rt, r, l);
				rangecheck(x.lb, r, l);
			}
			else if (x.p.x() >= r.xmax()) rangecheck(x.lb, r, l);
			else if (x.p.x() <= r.xmin()) rangecheck(x.rt, r, l);
		}
		
		if (x.isHorizontal) {
			if (x.p.y() >= r.ymin() && x.p.y() <= r.ymax()) {
				if (x.p.x() >= r.xmin() && x.p.x() <= r.xmax()) l.add(x.p);
				rangecheck(x.rt, r, l);
				rangecheck(x.lb, r, l);
			}
			else if (x.p.y() >= r.ymax()) rangecheck(x.lb, r, l);
			else if (x.p.y() <= r.ymin()) rangecheck(x.rt, r, l);
		}
	}
	
	public Point2D nearest(Point2D p) {
		if (p == null) throw new java.lang.IllegalArgumentException();
		return checknearest(root, p);
	}
	
	private Point2D checknearest(node x, Point2D s) {
		if (!x.isHorizontal) {
			if (s.x() < x.p.x()) {
				if (s.distanceTo(x.lb.p) < s.distanceTo(x.p)) x = x.lb;
				if (s.distanceTo(x.lb.p) > s.distanceTo(x.p)) {
					s.
				}
			}
		}
	}
	
	public static void main(String[] args) {
    	KdTree ps = new KdTree();
    	ps.insert(new Point2D(0.5, 0.7));
    	ps.insert(new Point2D(0.2, 0.2));
    	ps.insert(new Point2D(0.8, 0.8));
        ps.insert(new Point2D(0.1, 0.6));  
        System.out.print(ps.size());
        System.out.println();
        ps.draw();
        RectHV a = new RectHV(0.2, 0.2, 0.9, 0.9);
        Iterable<Point2D> iter = ps.range(a);
        for (Point2D p : iter) {
        	System.out.println(p.x());
        }
    }
}
