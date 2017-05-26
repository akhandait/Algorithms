import java.util.Iterator;
public class Deque<Item> implements Iterable<Item> {
	private int n;
	private Node first = null;
	private Node last = null;
	
	private class Node
	{
		Item item;
		Node next, previous;
	}
	
	public Deque()
	{
		first = null;
		last = null;
		n = 0;
	}

	public boolean isEmpty()
	{
		return first == null;
	}
	
	public int size()
	{
		return n;
	}
	
	public void addFirst(Item item)
	{
		if(item == null) throw new NullPointerException();
		Node oldfirst = first;
		first = new Node();
		first.item = item;
		first.next = oldfirst;
		first.previous = null;
		n++;
		if(n == 1) last = first;
		else oldfirst.previous = first;
	}
	
	public void addLast(Item item)
	{
		if(item == null) throw new NullPointerException();
		Node oldlast = last;
		last = new Node();
		last.item = item;
		last.next = null;
		last.previous = oldlast;
		n++;
		if(isEmpty()) first = last;
		else oldlast.next = last;
	}
	
	public Item removeFirst()
	{
		if(n == 0) throw new java.util.NoSuchElementException();
		Item item = first.item;
		first = first.next;
		if(!isEmpty()) first.previous = null;
		if(isEmpty()) last = null;
		n--;
		return item;
	}
	
	public Item removeLast()
	{
		if(n == 0) throw new java.util.NoSuchElementException();
		Item item = last.item;
		if(n > 1) {last = last.previous;
		last.next = null;}
        if(n==1) {first = null;
        last = null;
        }
		n--;
		return item;
	}
	
	public Iterator<Item> iterator()
	{
		return new ListIterator();
	}
	private class ListIterator implements Iterator<Item>
	{
		private Node current = first;
		
		public boolean hasNext()
		{
			return current != null;
		}
		public void remove() {throw new UnsupportedOperationException();}
		public Item next()
		{
			if(current == null) throw new java.util.NoSuchElementException();
			Item item = current.item;
			current = current.next;
			return item;
		}
	}
}
