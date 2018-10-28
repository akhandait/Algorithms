import java.util.Arrays;
import java.util.ArrayList;
//import edu.princeton.cs.algs4.StdDraw;
//import edu.princeton.cs.algs4.StdOut;

public class FastCollinearPoints {
    
	private ArrayList<LineSegment> lineSegments = new ArrayList<LineSegment>();
	
	public FastCollinearPoints(Point[] points) {
		if (points == null) throw new java.lang.IllegalArgumentException();
		for (int i = 0; i < points.length; i++) {
			if (points[i] == null) 
				throw new java.lang.IllegalArgumentException();
		}
		
		// Auxiliary array of sorted points.
		Point[] aux = Arrays.copyOf(points, points.length);
		int min, max;

		for (int i = 0; i < points.length; i++) {
			Arrays.sort(aux);
			Arrays.sort(aux, points[i].slopeOrder());
			
			if (aux[0].compareTo(aux[1]) == 0) {
				throw new java.lang.IllegalArgumentException();
			}

			for (min = 1; min < aux.length - 1; min++) {
				if (aux[0].slopeTo(aux[min]) == aux[0].slopeTo(aux[min + 1])) {
					max = min;
					
					while (aux[0].slopeTo(aux[max]) == 
						aux[0].slopeTo(aux[max + 1])) {
						max++;
					    if (max == aux.length - 1) break;    
					}
					
					if (max - min >= 2 && aux[0].compareTo(aux[min]) != 1) {
						lineSegments.add(new LineSegment(aux[0], aux[max]));
					}
					min = max;
				}
			}
		}
	}
	
	public int numberOfSegments() {
		return lineSegments.size();
	}
	
	public LineSegment[] segments() {
		LineSegment[] segments = new LineSegment[numberOfSegments()];
		segments = lineSegments.toArray(segments);		
		return segments;
	}
	
	public static void main(String[] args) {
//		// read the n points from a file
//		int n = Integer.parseInt(args[0]);
//		Point[] points = new Point[n];
//		
//		int x, y;
//		for (int i = 0; i < n; i++) {
//		    x = Integer.parseInt(args[2 * i + 1]);
//		    y = Integer.parseInt(args[2 * i + 2]);
//		    points[i] = new Point(x, y);
//		}
//		
//	    // draw the points
//	    StdDraw.enableDoubleBuffering();
//	    StdDraw.setXscale(0, 32768);
//	    StdDraw.setYscale(0, 32768);
//	    StdDraw.setPenRadius(0.01);
//	    StdDraw.setPenColor(StdDraw.BLACK);
//	    for (Point p : points) {
//	        p.draw();
//	    }
//	    StdDraw.show();
//
//	    // print and draw the line segments
//	    FastCollinearPoints collinear = new FastCollinearPoints(points);
//	    StdOut.println("Number of segments -> " + collinear.segments().length);
//	    StdDraw.setPenRadius(0.003);
//	    for (LineSegment segment : collinear.segments()) {
//	        StdOut.println(segment);
//	        segment.draw();
//	    }
//	    StdDraw.show();
	}
}
