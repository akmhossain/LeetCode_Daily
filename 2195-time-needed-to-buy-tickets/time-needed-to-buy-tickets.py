class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        # people can leave the line
        # loop through list while true
            # if we are at k chseck if its 0 : return total
            # if ptr is at end of list reset to 0
            # if curr pos is 0, skip without adding else add one to total
        
        res = 0
        ptr = 0

        while True:
            if ptr == k:
                tickets[ptr] -= 1
                if tickets[ptr] == 0:
                    return res + 1
                else:
                    res += 1
                    ptr += 1
            else:
                if tickets[ptr] == 0:
                    ptr += 1
                    pass
                else:
                    tickets[ptr] -= 1
                    res += 1
                    ptr += 1
            if ptr == len(tickets):
                ptr = 0

# 232
# 121
# 010
# 000