# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # while list1 and list 2, add and carry 1 if >10
        carry = 0
        resList = ListNode()
        curr = resList

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            sum_val = val1 + val2 + carry
            if sum_val >= 10:
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(sum_val % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return resList.next