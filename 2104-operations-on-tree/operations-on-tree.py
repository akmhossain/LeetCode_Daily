from collections import defaultdict
from collections import deque

class LockingTree:
    # invariant that there will be n nodes
    def __init__(self, parent: List[int]):
        self.parent = parent 
        self.d_map = defaultdict(list) # descendant map parent --> child
        self.lock_map = [None] * len(parent) # node is index, None if unlocked, user# if locked

        for child, parent in enumerate(parent):
            if child == 0:
                continue
            self.d_map[parent].append(child)

    def lock(self, num: int, user: int) -> bool:
        if self.lock_map[num]:
            return False
        
        self.lock_map[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.lock_map[num] != user:
            return False
        
        self.lock_map[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.lock_map[num]:
            return False

        ptr = self.parent[num]
        while ptr != -1: # check all parents are unlocked
            if self.lock_map[ptr]:
                return False
            ptr = self.parent[ptr]
        
        # unlock all desendants using q, keep track if atleast one was unlocked
        unlocked = False
        q = deque([num])
        while q:
            node = q.popleft()
            if self.lock_map[node]:
                unlocked = True
                self.lock_map[node] = None
            for i in self.d_map[node]:
                q.append(i)
        
        if unlocked:
            self.lock_map[num] = user
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)