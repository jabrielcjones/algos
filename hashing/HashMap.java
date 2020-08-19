import java.util.*;
import java.io.*;

class HashMap {
	private int size;
	private LinkedList[] map;


	HashMap() {
		this.size = 10;
		this.map = new LinkedList[this.size];

		for (int i = 0; i < this.size; i++)
			this.map[i] = null;
	}

	private int getHash(String key) {
		int hash = 0;

		for (int i = 0; i < key.length(); i++) {
			hash += (int) key.charAt(i);
		}

		return hash % this.size;
	}

	public boolean add(String key, String value) {

		int key_hash = getHash(key);
		String[] key_value = {key, value};

		if (this.map[key_hash] == null) {
			this.map[key_hash] = new LinkedList();
			this.map[key_hash].push(key_value);

			return true;
		}
		else {
			if (this.map[key_hash].search(key))
				return true;

			this.map[key_hash].push(key_value);

			return true;
		}

	}

	public String get(String key) {
		int key_hash = getHash(key);
		String value = "";

		if (this.map[key_hash] != null) {
			return this.map[key_hash].get(key);
		}

		return null;
	}

	public void display() {
		for (int i = 0; i < this.size; i++) {
			if (map[i] == null)
				System.out.println(i + ". " + map[i]);

			else {
				System.out.print(i + ". ");
				map[i].printList();
			}

			System.out.println();
		}
	}

	public static void main(String[] args) {
    	HashMap h = new HashMap();

    	// h.display();

    	h.add("Jabriel", "05/30/1991");
		h.add("Nobi", "06/24/1991");
		h.add("Nina", "10/27/2019");
		h.add("Lamont", "mm/dd/yyyy");
		h.add("Zyon", "mm/dd/yyyy");
		h.add("Branden", "mm/dd/yyyy");
		h.add("Corbin", "mm/dd/yyyy");
		h.add("Natera", "mm/dd/yyyy");
		h.add("Lamuel", "mm/dd/year");
		h.add("Kaza", "mm/dd/yyyy");

		h.display();

		System.out.println(h.get("Lamuel"));

		// Test 1 - Duplicate Keys
		// h.add("Jabriel", "05/30/1991");
		// h.add("Nobi", "06/24/1991");
		// h.add("Nina", "10/27/2019");
		// h.add("Lamont", "mm/dd/yyyy");
		// h.add("Zyon", "mm/dd/yyyy");
		// h.add("Branden", "mm/dd/yyyy");
		// h.add("Corbin", "mm/dd/yyyy");
		// h.add("Natera", "mm/dd/yyyy");
		// h.add("Lamuel", "mm/dd/yyyy");
		// h.add("Kaza", "mm/dd/yyyy");

		// h.display();
    }
}