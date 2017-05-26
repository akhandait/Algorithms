import edu.princeton.cs.algs4.*;
import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> {
	private Item[] A;
	private int n = 0;
	public RandomizedQueue()
	{
		A = (Item[]) new Object[1];
	}
	
	public boolean isEmpty()
	{
		return n==0;
	}

	public int size()
	{
		return n;
	}
	
	public void enqueue(Item item)
	{
		if(item == null) throw new NullPointerException();
		if(n == A.length) resize(2*A.length);
		A[n] = item;
		n++;
	}
	
	private void resize(int capacity)
	{
		Item[] copy = (Item[]) new Object[capacity];
		for(int i=0; i < n; i++)
		{
			copy[i] = A[i];
		}
		A = copy;
	}
	
	public Item dequeue()
	{
		if(n == 0) throw new java.util.NoSuchElementException();
		int r = StdRandom.uniform(n);
		swap(r, n-1);
		Item ret = A[n-1];
		A[n-1] = null;
		n--;
		if (n == A.length/4 && n!= 0) resize(A.length/2);
		return ret;
	}
	
	private void swap(int a, int b)
	{
		Item temp = A[a];
		A[a] = A[b];
		A[b] = temp;
	}
	
	public Item sample()
	{
		if(n == 0) throw new java.util.NoSuchElementException();
		int r = StdRandom.uniform(n);
		return A[r];
	}
	
	public Iterator<Item> iterator()
	{
		return new RAIterator();
	}
	
	private class RAIterator implements Iterator<Item>
	{
		private int p = n;
		private Item[] B = A;
		public boolean hasNext()
		{
			return p > 0;
		}
		public void remove()
		{
			throw new java.lang.UnsupportedOperationException();
		}
		public Item next()
		{
			if(!hasNext()) throw new java.util.NoSuchElementException();
			int r = StdRandom.uniform(p);
			swap(r, p-1); Item ret = B[p-1]; p--;
			return ret;
		}
	}
}
