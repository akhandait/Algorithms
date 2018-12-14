import java.util.Iterator;
import edu.princeton.cs.algs4.StdOut;

public class Deque<Item> implements Iterable<Item> {

    private Node first, last;
    private int size;

    private class Node {
        Item item;
        Node next;
        Node previous;
    }

    public Deque() {
        size = 0;
        first = null;
        last = null;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public void addFirst(Item item) {
        if (item == null) throw new IllegalArgumentException();

        size++;
        Node oldFirst = first;

        first = new Node();
        first.item = item;
        first.next = oldFirst;
        first.previous = null;

        if (size > 1) oldFirst.previous = first;
        else last = first;
    }

    public void addLast(Item item) {
        if (item == null) throw new IllegalArgumentException();

        size++;
        Node oldLast = last;

        last = new Node();
        last.item = item;
        last.next = null;
        last.previous = oldLast;

        if (size > 1) oldLast.next = last;
        else first = last;
    }

    public Item removeFirst() {
        if (size == 0) throw new java.util.NoSuchElementException();

        size--;
        Item item = first.item;
        first = first.next;

        if (size >= 1) first.previous = null;
        else last = null;

        return item;
    }

    public Item removeLast() {
        if (size == 0) throw new java.util.NoSuchElementException();

        size--;
        Item item = last.item;
        last = last.previous;

        if (size >= 1) last.next = null;
        else  first = null;

        return item;
    }

    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) throw new java.util.NoSuchElementException();

            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) {
        // Deque<Integer> d = new Deque<Integer>();
        // d.addFirst(4);
        // d.addLast(3);
        // d.addFirst(2);
        // d.addFirst(6);
        // StdOut.println(d.removeFirst());
        // StdOut.println(d.removeLast());
        // StdOut.println(d.removeLast());
        // StdOut.println(d.removeLast());
        // d.addFirst(6);
        // StdOut.println(d.removeLast());

        // for (int s : d) {
        //  StdOut.println(s);
        // }
    }
}
