class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # sort and greedy approach
        # two pointer - l/r
        # nlogn time

        people.sort()

        l,r = 0,len(people)-1
        res = 0

        while l <= r: # needs to be equal for odd number of people case
            if people[l] + people[r] <= limit:
                l += 1 # fit every lighter person

            r -= 1 # heaver person gets on boat
            res += 1
        
        return res

        # 3 3 4 5