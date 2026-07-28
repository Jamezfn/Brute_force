import { LinkedList } from "./linkedlist.js";

export function createLinkedList(...values: number[]) {
	const ll = new LinkedList();

	for (let i = values.length - 1; i >= 0; i--) {
		ll.insertAtHead(values[i]!);
	}

	return ll;
}