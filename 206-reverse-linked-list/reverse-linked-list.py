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
        curr = head
        prev = None

        while curr:
            # temp = None
            temp = curr.next
            # next = None
            curr.next = prev
            # prev = 1
            prev = curr
            # None
            curr = temp
        
        return prev

 
