# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # while list1 or list2, if list 1 or list 1, if list 1 and list 2
        resList = ListNode(val=None)
        head = resList   

        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    resList.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    resList.next = ListNode(list1.val)
                    list1 = list1.next
            elif list1:
                resList.next = ListNode(list1.val)
                list1 = list1.next
            else:
                resList.next = ListNode(list2.val)
                list2 = list2.next
            
            resList = resList.next

        return head.next

