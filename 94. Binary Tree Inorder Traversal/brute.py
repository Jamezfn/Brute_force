from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		res = []

		def bfs(root: Optional[TreeNode]):
			if not root:
				return

			bfs(root.left)
			res.append(root.val)
			bfs(root.right)

		bfs(root)

		return res