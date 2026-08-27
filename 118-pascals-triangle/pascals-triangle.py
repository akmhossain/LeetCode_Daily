class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # base cases: row 0 - [1], row 1 - [1,1], row 2 - [1,x,1]

        row0, row1 = [1], [1, 1]
        if numRows == 1: return [row0]
        if numRows == 2: return [row0, row1]
        
        dp = [row0, row1]
        for i in range(3, numRows+1):
            lvl = [1]
            last_lvl = dp[-1]
            for j in range(len(last_lvl) - 1):
                next_ = last_lvl[j] + last_lvl[j+1]
                lvl.append(next_)
            lvl.append(1)
            dp.append(lvl)
        
        return dp