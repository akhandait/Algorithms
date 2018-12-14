import java.util.Iterator;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {

    private Item[] array;
    private int size;

    public RandomizedQueue() {
        array = (Item[]) new Object[1];
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public void enqueue(Item item) {
        if (item == null) throw new IllegalArgumentException();

        if (size == array.length) resize(2 * array.length);
        array[size++] = item;
    }

    public Item dequeue() {
        if (size == 0) throw new java.util.NoSuchElementException();

        int random = StdRandom.uniform(size);
        swap(random, size - 1);

        Item item = array[--size];
        array[size] = null;
        if (size > 0 && size == array.length / 4) resize(array.length / 2);
        return item;
    }

    public Item sample() {
        if (size == 0) throw new java.util.NoSuchElementException();

        int random = StdRandom.uniform(size);
        return array[random];
    }

    private void resize(int capacity) {
        Item[] arraytemp = (Item[]) new Object[capacity];
        for (int i = 0; i < size; i++) {
            arraytemp[i] = array[i];
        }
        array = arraytemp;
    }

    private void swap(int index1, int index2) {
        Item temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Item[] arrayTemp;
        private int current;

        public ListIterator() {
            arrayTemp = (Item[]) new Object[size];
            for (int i = 0; i < size; i++) {
                arrayTemp[i] = array[i];
            }
            current = size;
        }

        public boolean hasNext() {
            return current > 0;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) throw new java.util.NoSuchElementException();

            int random = StdRandom.uniform(current);
            swap(random, current - 1);
            return arrayTemp[--current];
        }

        private void swap(int index1, int index2) {
            Item temp = arrayTemp[index1];
            arrayTemp[index1] = arrayTemp[index2];
            arrayTemp[index2] = temp;
        }
    }

    public static void main(String[] args) {
        // RandomizedQueue<Integer> rq = new RandomizedQueue<Integer>();
        // rq.enqueue(4);
        // rq.enqueue(3);
        // rq.enqueue(2);
        // rq.enqueue(6);
        // for (int i = 0; i < 5; i++) {
        //     StdOut.println(rq.dequeue());
        // }
        // StdOut.println(rq.sample());

        // for (int s : rq) {
        //     StdOut.println(s);
        // }
    }
}
