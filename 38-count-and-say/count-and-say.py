class Solution:
    def countAndSay(self, n: int) -> str:
        # base case: 1
        
        def getRLE(s):
            count = 0
            curr_num = s[0]
            res = ""

            # s = 11
            for i in range(len(s)):
                if s[i] == curr_num:
                    count += 1
                else:
                    res += str(count)
                    res += curr_num
                    count, curr_num = 1, s[i]
            
            if count > 0:
                res += str(count)
                res += curr_num

            return res

        RLE = "1" # 11
        for i in range(n-1):
            RLE = getRLE(RLE)
        
        return RLE

            