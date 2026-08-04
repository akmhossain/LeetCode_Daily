class Solution:
    operators = {'+':lambda x,y: x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y} # avoid rebuilding hash every call

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # build solution around operators - what determines the last operation
        
        res = []

        for i in range(len(expression)):
            if expression[i] in self.operators: # split at operators
                leftList = self.diffWaysToCompute(expression[:i]) # left until operator-excluded
                rightList = self.diffWaysToCompute(expression[i+1:])
            
                # join left and right list
                for n1 in leftList:
                    for n2 in rightList:
                        res.append(self.operators[expression[i]](n1, n2))

        # base case: integer, check empty since recursion happens only at operators
        if res == []:
            res.append(int(expression))

        return res
    
