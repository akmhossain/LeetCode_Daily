# Doubly Linked List Implementation
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    # implement linked list and array 
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr) # set next page
        self.curr = self.curr.next # traverse to next page

    def back(self, steps: int) -> str:
        # check inbounds: only iterate until head is reached 
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        # check inbound: only iterate until tail
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        
# Time complexity:
# visit - O(1) since it just changes pointer direction
# back/forward: O(n) at worst its possible to traverse entire list

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)