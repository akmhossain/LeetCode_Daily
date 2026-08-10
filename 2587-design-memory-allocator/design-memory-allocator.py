class Allocator:
    # invariant that the size will never change
    # brute force solution: mark all unused spaces -1, and used mID spaces with mID
    def __init__(self, n: int):
        self.mem = [-1] * n # -1 to denote free space
        self.mem_size = n

    def allocate(self, size: int, mID: int) -> int:
        free = 0 # track number of free spaces at an opening
        for i in range(self.mem_size):
            if self.mem[i] == -1:
                free += 1
            else:
                free = 0 # reset count if not enough
            
            if free == size: # enough space found
                for j in range(i-size+1, i+1):
                    self.mem[j] = mID
                return i-size+1
        return -1 # worst case no spot found iterated through entire memory

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.mem_size): 
            if self.mem[i] == mID:
                self.mem[i] = -1
                count += 1
        return count

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)