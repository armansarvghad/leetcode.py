class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        def dfs(node, curr_number):
            if not node:
                return 0
            curr_number = curr_number * 10 + node.val
            if not node.left and not node.right:
                return curr_number
            return dfs(node.left, curr_number) + dfs(node.right, curr_number)

        return dfs(root, 0)