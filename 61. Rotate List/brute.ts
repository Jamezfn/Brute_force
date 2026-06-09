/**
 * singly-linked list.
 *
 */

class ListNode {
	val: number
	next: ListNode | null

	constructor(val?: number, next?: ListNode | null) {
		this.val = (val === undefined ? 0 : val);
		this.next = (next === undefined ? null : next);
	}

	static listToLinkedList(nums: number[]): ListNode | null {
		if (nums.length === 0) {
			return null;
		}

		const head = new ListNode(nums[0]);
		let cur = head;

		for (let i = 1; i < nums.length; i++) {
			cur.next =  new ListNode(nums[i]);
			cur = cur.next;
		}

		return head;
	}

	linkedListToList(): number[] {
		const nums: number[] = [];
		let cur: ListNode | null = this;

		while (cur) {
			nums.push(cur.val);
			cur = cur.next;
		}

		return nums;
	}

	static rotateRight(head: ListNode | null, k: number): ListNode | null {
		if (!head) {
			return head;
		}

		let len = 1;
		let tail = head;

		while (tail.next) {
			tail = tail.next;
			len++;
		}

		k = k % len;

		if (k === 0) {
			return head;
		}

		let cur = head;

		for (let i = 0; i < len - k - 1; i++) {
			cur = cur.next!;
		}

		const newHead = cur.next!;
		cur.next = null;
		tail.next = head;

		return newHead;
	}
}

const h = [1, 2, 3, 4, 5];
const head = ListNode.listToLinkedList(h);
const r = ListNode.rotateRight(head, 2);
console.log(r?.linkedListToList())
