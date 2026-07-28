import { createLinkedList } from "./helper.js";
import { LinkedList } from "./linkedlist.js";

describe("#insertAtHead", () => {
	test("Adds the element to the beginning of the list", () => {
		const ll = new LinkedList();
		ll.insertAtHead(10);
		const oldHead = ll.head;
		ll.insertAtHead(20);

		expect(ll.head?.value).toBe(20);
		expect(ll.head?.next).toBe(oldHead);
		expect(ll.len).toBe(2);
	})
});

describe("#getByIndex", () => {
	describe("With index less than zero", () => {
		test("It returns null", () => {
			const ll = createLinkedList(10, 20)

			expect(ll.getByIndex(-1)).toBeNull()
		})
	});

	describe("With index greater than list length", () => {
		test("It returns null", () => {
			const ll = createLinkedList(10, 20)

			expect(ll.getByIndex(5)).toBeNull();
		})
	});

	describe("With index zero", () => {
		test("It returns the head", () => {
			const ll = createLinkedList(10, 20);

			expect(ll.getByIndex(0)?.value).toBe(10);
		})
	});

	describe("With index in the middle", () => {
		test("It returns the element at that index", () => {
			const ll = createLinkedList(10, 20, 30, 40);

			expect(ll.getByIndex(2)?.value).toBe(30);
		})
	});
});

describe("#insertAtIndex", () => {
	describe("With index less than zero", () => {
		test("It does not insert anything", () => {
			const ll = createLinkedList(10, 20);

			ll.insertAtIndex(-1, 30);

			expect(ll.len).toBe(2);
		});
	});

	describe("With index greater than list length", () => {
		test("It does not insert anything", () => {
			const ll = createLinkedList(10, 20);

			ll.insertAtIndex(5, 30);

			expect(ll.len).toBe(2);
		});
	});

	describe("With index zero", () => {
		test("Insert at the head", () => {
			const ll = createLinkedList(10, 20);
			ll.insertAtIndex(0, 30);

			expect(ll.head?.value).toBe(30);
			expect(ll.head?.next?.value).toBe(10);
			expect(ll.len).toBe(3);
		});
	});

	describe("With index in the middle", () => {
		test("Insert at a given index", () => {
			const ll = createLinkedList(10, 20, 30, 40);
			ll.insertAtIndex(2, 50);
			const node = ll.getByIndex(2);

			expect(node?.value).toBe(50);
			expect(node?.next?.value).toBe(30);
			expect(ll.len).toBe(5);
		});
	});
})

describe("#removeHead", () => {
	test("Removes the head", () => {
		const ll = createLinkedList(10, 20, 30);
		ll.removeHead();

		expect(ll.head?.value).toBe(20);
		expect(ll.len).toBe(2);
	})
})

describe("#removeAtIndex", () => {
	describe("With index less than zero", () => {
		test("It does not remove anything", () => {
			const ll = createLinkedList(10, 20);

			ll.removeAtIndex(-1);

			expect(ll.len).toBe(2);
		});
	});

	describe("With index greater than list length", () => {
		test("It does not remove anything", () => {
			const ll = createLinkedList(10, 20);

			ll.removeAtIndex(50);

			expect(ll.len).toBe(2);
		});
	});

	describe("With index zero", () => {
		test("Remove the head", () => {
			const ll = createLinkedList(10, 20, 30);
			ll.removeAtIndex(0);

			expect(ll.head?.value).toBe(20);
			expect(ll.head?.next?.value).toBe(30);
			expect(ll.len).toBe(2);
		});
	});

	describe("With index in the middle", () => {
		test("Remove at a given index", () => {
			const ll = createLinkedList(10, 20, 30, 40);
			ll.removeAtIndex(2);
			const node = ll.getByIndex(1);

			expect(node?.value).toBe(20);
			expect(node?.next?.value).toBe(40);
			expect(ll.len).toBe(3);
		});
	});
})