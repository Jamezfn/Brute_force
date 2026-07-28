import { createLinkedList } from "./helper.js";

const ll = createLinkedList(10, 20, 30, 40);
ll.print();
console.log(ll.getByIndex(2)?.value);