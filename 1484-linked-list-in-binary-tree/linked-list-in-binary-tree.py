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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # loop until path matches(true) or whole tree traversed(false)
        # start moving forward tree if node val matches list val
          # if at end of list then return true

        # create a match function that sees if there is a match going down for ALL nodes
        def match(head, root):
            if not head:
                return True
            if not root:
                return False
            if root.val == head.val:
                return match(head.next, root.left) or match(head.next, root.right)
            else:
                return False

        if not root:
           return False
        
        if root.val == head.val and match(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

            
