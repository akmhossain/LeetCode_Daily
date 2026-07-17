from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employee_dict = defaultdict(list) # parent to children {int:list[int]}
        for child,parent in enumerate(manager): # index(current child), int(parent) 
            if child == headID:
                continue
            employee_dict[parent].append(child)
        
        res = 0
        def dfs(node, currMax):
            nonlocal res
            if not employee_dict[node]: # if leaf
                res = max(res, currMax)
                return 
            for child in employee_dict[node]:
                dfs(child, currMax + informTime[child])
        
        dfs(headID, informTime[headID])
        return res

        # h = {2:[0,1,3,4,5], 1:[6]}

        # # parent --> child traversal
        # def dfs(node):
        #     for child in employee_dict[node]:
        #         print(child)
        #         dfs(child)






            