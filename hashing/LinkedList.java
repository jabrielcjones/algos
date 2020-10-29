import java.io.*;

class Node {
	String[] key_value;
	Node next;

	Node(String[] kv) {
		this.key_value = kv;
		this.next = null;
	}
}

class LinkedList {
	Node head = null;

	public void push(String key_value[]) {
		// Allocate new node and store key_value
		Node new_node = new Node(key_value);

		// Point new node to the old head
		new_node.next = this.head;

		// Make the new node the new head
		this.head = new_node;
		
	}

	public boolean search (String key) {
		Node current = this.head;

		while (current != null) {
			if (current.key_value[0] == key)
				return true;

			current = current.next;
		}
		return false;
	}

	public String get(String key) {
		Node current = this.head;

		while (current != null) {
			if (current.key_value[0] == key)
				return current.key_value[1];

			current = current.next;
		}
		return null;
	}

	public boolean remove(String key) {
		if (this.head.key_value[0] == key) {
			this.head = this.head.next;
			return true;
		}
		else {
			Node current = this.head.next;
			Node previous = this.head;

			while (current != null) {
				if (current.key_value[0] == key) {
					previous.next = current.next;
					return true;
				}

				previous = current;
				current = current.next;
			}
			return false;
		}
	}

	public void printList() {
		Node current = this.head;

		System.out.print("LinkedList:\n");

		while (current != null) {
			for (int i = 0; i < current.key_value.length; i++)
				System.out.print(current.key_value[i] + " ");

			System.out.print("\n");

			current = current.next;
		}
	}

	public static void main(String args[]) {
		LinkedList llist = new LinkedList();

		llist.push(new String[]{"jabriel", "05/30/1991"});

		System.out.print(llist.search("jabriel") + "\n");

		llist.printList();
	}
}