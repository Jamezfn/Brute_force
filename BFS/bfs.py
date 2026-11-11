#!/usr/bin/env python

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        curr = queue.popleft()
        result.append(curr.value)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return result
