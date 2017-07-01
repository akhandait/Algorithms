import java.util.Arrays;
import java.util.ArrayList;

public class BruteCollinearPoints {

	private ArrayList<LineSegment> lines = new ArrayList<LineSegment>();
	
	public BruteCollinearPoints(Point[] points) {
		if(points == null) throw new java.lang.NullPointerException();
		
		Arrays.sort(points);
		for (int i = 0; i < points.length; i++) {
			if (points[i] == null) throw new java.lang.NullPointerException();
			
			for (int j = i + 1; j < points.length; j++) {
				if(points[i].compareTo(points[j]) == 0) throw new java.lang.IllegalArgumentException();
				
				for (int k = j + 1; k < points.length; k++) {
					for (int h = k + 1; h < points.length; h++) {
						if (points[i].slopeTo(points[j]) == points[i].slopeTo(points[k]) && points[i].slopeTo(points[j]) == points[i].slopeTo(points[h]) ) {
							LineSegment l = new LineSegment(points[i], points[h]);
							lines.add(l);
						}
					}
				}
			}
		}
	}
	
	public int numberOfSegments() {
		return lines.size();
	}
	
	public LineSegment[] segments() {
		LineSegment[] linesegments =  new LineSegment[lines.size()];
		linesegments = lines.toArray(linesegments);
		return linesegments;
	}
}
