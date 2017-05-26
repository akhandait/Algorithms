import edu.princeton.cs.algs4.*;

public class Percolation {
	
	private WeightedQuickUnionUF uf;	
	private int nos = 0;//keeps track of number of open sites
	private int[][]bsa;//tells if each element in the grid is blocked or unblocked
	private int q;
	
	public Percolation(int n)
	{
		if(n<=0) throw new IllegalArgumentException();
		uf = new WeightedQuickUnionUF(n*n+2);//the 2 extra are the virtual top and bottom sites respectively
		q = n;
		bsa = new int[n][n];//0 means blocked
	}
	
	public void open(int row,int col)
	{
		if(row-1<0 || row-1>=q || col-1<0 || col-1>=q) throw new IndexOutOfBoundsException();
		if(bsa[row-1][col-1] == 1) return;
		if(row == 1) uf.union(q*q, col-1);
		if(row == q) uf.union(q*q+1, (row-1)*q+col-1);
		bsa[row-1][col-1] = 1;
		nos++;
		try{if(bsa[row-2][col-1] == 1) uf.union(((row-1)*q)+col-1,(row-2)*q+col-1);} catch(IndexOutOfBoundsException e){}
		try{if(bsa[row-1][col-2] == 1) uf.union((row-1)*q+col-1,(row-1)*q+col-2);}catch(IndexOutOfBoundsException e){}
		try{if(bsa[row][col-1] == 1) uf.union((row-1)*q+col-1,(row)*q+col-1);}catch(IndexOutOfBoundsException e){}
		try{if(bsa[row-1][col] == 1) uf.union((row-1)*q+col-1,(row-1)*q+col);}catch(IndexOutOfBoundsException e){}
	}

	public boolean isOpen(int row,int col)
	{
		if(row-1<0 || row-1>=q || col-1<0 || col-1>=q) throw new IndexOutOfBoundsException();
		if(bsa[row-1][col-1] == 1) return true;
		else return false;
	}
	
	public boolean isFull(int row,int col)
	{
		if(row-1<0 || row-1>=q || col-1<0 || col-1>=q) throw new IndexOutOfBoundsException();
		if(uf.connected((row-1)*q+col-1, q*q)) return true;
		else return false;
	}
	
	public int numberOfOpenSites()
	{
		return nos;
	}
	
	public boolean percolates()
	{
		if(uf.connected(q*q,q*q+1 )) return true;
		return false;
	}
	
	public static void main(String[] s)
	{
		Percolation p = new Percolation(3);
		p.open(1, 1);
		p.open(2, 1);
		p.open(2, 2);
		p.open(3, 3);
		if(p.percolates() == true) StdOut.print(21);
	}
}
