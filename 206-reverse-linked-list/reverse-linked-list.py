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
        # 1-->2 
        # reverseList(1), reverseList(2)

        if head == None:
            return head
        if head.next == None:
            return head 
        new_head = self.reverseList(head.next) # 2
        head.next.next = head
        head.next = None 

        return new_head
 
