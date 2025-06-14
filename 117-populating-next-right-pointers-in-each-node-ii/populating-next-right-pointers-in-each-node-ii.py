class Solution:
    def connect(self, root):
        if not root:
            return root
        
        head = root
        while head:
            dummy = Node(0)
            temp = dummy

            while head:
                if head.left:
                    dummy.next = head.left
                    dummy = dummy.next
                if head.right:
                    dummy.next = head.right
                    dummy = dummy.next
                head = head.next

            head = temp.next
        return root