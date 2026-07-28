export class LinkedList {
	head:LinkedListNode | null;
	len: number;

	constructor() {
		this.head = null;
		this.len = 0;
	}

	insertAtHead(data: number) {
		const newNode = new LinkedListNode(data, this.head);
		this.head = newNode;
		this.len++;
	}

	getByIndex(index: number): LinkedListNode | null {
		if (index < 0 || index >= this.len) return null;

		let cur = this.head;
		for (let i = 0; i < index; i++) {
			cur = cur?.next!;
		}

		return cur;
	}

	insertAtIndex(index: number, value: number): void {
		if (index === 0) return this.insertAtHead(value);

		const prev = this.getByIndex(index - 1);

		if (prev === null) return;

		prev.next = new LinkedListNode(value, prev.next);
		this.len++;
	}

	removeHead(): void {
		this.head = this.head ? this.head?.next : null;
		this.len--;
	}

	removeAtIndex(index: number): void {
		if (index === 0) return this.removeHead();

		const prev = this.getByIndex(index - 1);
		if (prev === null) return;

		prev.next = prev.next ? prev.next?.next : null;
		this.len--;
	}

	print() {
		let output = "";
		let cur = this.head;

		while (cur) {
			output = `${output}${cur.value} -> `
			cur = cur.next
		}

		console.log(`${output}null`)
	}
}

class LinkedListNode {
	value: number;
	next: LinkedListNode | null;
	constructor(value: number, next: LinkedListNode | null = null) {
		this.value = value;
		this.next = next;
	}
}