import java.util.Arrays;
import edu.princeton.cs.algs4.StdOut;
import java.util.ArrayList;

public class BruteCollinearPoints {
    
	private ArrayList<LineSegment> lineSegments = new ArrayList<LineSegment>();
	
	public BruteCollinearPoints(Point[] points) {
		if (points == null) throw new java.lang.IllegalArgumentException();
		for (int i = 0; i < points.length; i++) {
			if (points[i] == null) 
				throw new java.lang.IllegalArgumentException();
		}
		
		Point[] pointsSort = Arrays.copyOf(points, points.length);
		Arrays.sort(pointsSort);
	
		for (int i = 0; i < pointsSort.length; i++) {
			for (int j = i + 1; j < pointsSort.length; j++) {
				if (pointsSort[i].compareTo(pointsSort[j]) == 0) {
					throw new java.lang.IllegalArgumentException();
				}
				
				for (int k = j + 1; k < points.length; k++) {
					for (int l = k + 1; l < points.length; l++) {
						if (pointsSort[i].slopeTo(pointsSort[j]) == 
						    pointsSort[i].slopeTo(pointsSort[k]) && 
							pointsSort[i].slopeTo(pointsSort[j]) == 
							pointsSort[i].slopeTo(pointsSort[l])) {
							lineSegments.add(new LineSegment(pointsSort[i], 
								pointsSort[l]));
						}
					}
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
		int n = Integer.parseInt(args[0]);
		Point[] points = new Point[n];
		
		int x, y;
		for (int i = 0; i < n; i++) {
		    x = Integer.parseInt(args[2 * i + 1]);
		    y = Integer.parseInt(args[2 * i + 2]);
		    points[i] = new Point(x, y);
		}
		
		BruteCollinearPoints brute = new BruteCollinearPoints(points);
		StdOut.println(brute.segments());
	}
}
