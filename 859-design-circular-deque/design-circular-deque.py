# linked list implementation
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:
    # invariants: number of elements dont exceed k
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # empty deque
        if self.isEmpty():
            self.head = Node(value, None, None)
            self.tail = self.head
        else: 
            self.head.prev = Node(value, None, self.head)
            self.head = self.head.prev

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # empty deque
        if self.isEmpty():
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        # check if empty
        if self.isEmpty():
            return False
        if self.size == 1:
            # delete head and tail
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self.size -=1
        return True

    def deleteLast(self) -> bool:
        # check if empty
        if self.isEmpty():
            return False
        if self.size == 1:
            # delete head and tail
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev 
        
        self.size -=1
        return True

    def getFront(self) -> int:
          # check if empty
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        # check if empty
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.max_size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()