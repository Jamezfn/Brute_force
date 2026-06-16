class ListNode {
	val: number
	next: ListNode | null

	constructor(val?: number, next?: ListNode) {
		this.val = (val === undefined ? 0 : val);
		this.next = (next === undefined ? null : next);
	}

	toLinkedList(nums: number[]): ListNode | null {
		if (nums.length === 0) return null;

		const head = new ListNode(nums[0]);

		let cur = head;
		for (let i = 1; i < nums.length; i++) {
			cur.next = new ListNode(nums[i]);
			cur = cur.next;
		}

		return head;
	}

	toList(head: ListNode | null): number[] {
		const nums: number[] = [];

		let cur = head;
		while (cur) {
			nums.push(cur.val);
			cur = cur.next;
		}

		return nums;
	}

	deleteDuplicates(head: ListNode | null): ListNode | null {
		const dummy = new ListNode(0, head);
		let prev = dummy;

		let cur = head;
		while (cur) {
			if (cur.val === cur.next?.val ) {
				const val = cur.val;

				while (cur?.val === val) {
					cur = cur.next;
				}

				prev.next = cur;

			} else {
				prev = cur;
				cur = cur.next
			}
		}

		return dummy.next;
	}
}

const node = new ListNode();

const head = node.toLinkedList([1, 2, 3, 3, 4, 4, 5]);

const result = node.deleteDuplicates(head);

console.log(node.toList(result));
