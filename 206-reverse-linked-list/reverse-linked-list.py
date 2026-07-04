# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # reverse the arrows
        c = head
        p = None

        while c:
            temp = c.next # store next so we dont lose the list
            c.next = p # reverses arrow
            # move pointers forward
            p = c 
            c = temp
        
        return p
 
