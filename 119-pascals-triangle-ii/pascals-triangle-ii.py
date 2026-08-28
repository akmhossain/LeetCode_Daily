class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]

        res = [[1], [1,1]]

        for i in range(3, rowIndex+2):
            lvl = [1]
            prev_lvl = res[-1]
            for j in range(len(prev_lvl) - 1):
                lvl.append(prev_lvl[j] + prev_lvl[j+1])
            lvl.append(1)
            res.append(lvl)
        
        return res[-1]
        