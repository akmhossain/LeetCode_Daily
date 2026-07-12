# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # if not node/all nodes visited: return res
        # add val to curr_list, subtract from curr_sum
          # if leaf node:
           # if target sum = 0, append curr_list to res
           # else clear curr_list and reset curr_sum
        # dfs (left or right)
        res = []
        curr_path = []
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_path.append(node.val)
            curr_sum -= node.val

            if not node.right and not node.left:
                if curr_sum == 0:
                    res.append(list(curr_path)) # returns copy not reference
            else: # dfs - left(left(left)) first then right(right(right))
                dfs(node.left, curr_sum)
                dfs(node.right, curr_sum)
            
            curr_path.pop() # runs when each call executed 
        
        dfs(root, targetSum)
        return res

    # dfs(node):
    #   push node.val              <- runs immediately
    #   if leaf:
    #     check/save             <- runs immediately (if this branch taken)
    #   else:
    #     dfs(node.left)         <- runs immediately... but this pauses everything below until it returns
    #     dfs(node.right)        <- WAITS until dfs(node.left) fully finishes
    #   pop                         <- WAITS until dfs(node.right) fully finishes (or check/save, if leaf)




          
        