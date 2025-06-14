# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        level_start = root

        while level_start.left:
            current = level_start

            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next

            level_start = level_start.left

        return root