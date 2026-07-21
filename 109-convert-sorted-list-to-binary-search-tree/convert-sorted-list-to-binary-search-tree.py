# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        def BST(start, end):
            if start == end:
                return None
            
            slow = fast = start

            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
                # after while loop executes, slow will be in the middle and fast is at the end

            # repeat steps above, building finding slow (middle) and spliting list in half
            root = TreeNode(slow.val)
            root.left = BST(start, slow)
            root.right = BST(slow.next, end)

            return root
        
        return BST(head, None)