# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # implement the recursive call stack of dfs
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, root): 
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()

            if node.right:
                self.pushLeft(node.right)

            return node.val
        else:
            return None

    def hasNext(self) -> bool:
        # checks if traversal is done (if stack is empty all nodes traversed)
        return bool(self.stack)
       

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()