class Solution:
    def reverseBits(self, n: int) -> int:
        # convert to binary
        # flip then convert back

        def to_binary(num):
            if num == 0:
                return "0"
            res = ""
            while num > 0:
                if num % 2 == 0:
                    res += "0"
                else:
                    res += "1"
                num = num//2
            return res[::-1]
        
        def to_decimal(bin):
            idx = 1
            res = 0
            for i in range(len(bin) - 1, -1, -1):
                if bin[i] == "1":
                    res += idx
                idx = idx * 2
            
            return res

        binary = to_binary(n)
        binary = binary.zfill(32)

        return to_decimal(binary[::-1])