# Array Implementation
class BrowserHistory:
    # implement array w/ curr index pointer
    # init: list with just homepage
    # back/forward: check if steps inbound(steps is less than the curr index)
    # visit: slice the array if website is not the last element in the list, slice then append url
    
    def __init__(self, homepage: str):
      self.web = [homepage]
      self.curr = 0

    def visit(self, url: str) -> None: # branch off into new list 
        # if self.curr + 1 == len(self.web): # last element, no need to slice
        #     self.web.append(url)
        #     self.curr += 1
        # else: <-- Repetitive code
        self.web = self.web[:self.curr+1] # keep everything until curr
        self.web.append(url)
        self.curr = len(self.web) - 1 # set curr to new url

    def back(self, steps: int) -> str:
        if steps > self.curr: # more steps than elements back
            self.curr = 0
            return self.web[self.curr]
        else:
            self.curr -= steps
            return self.web[self.curr]

    def forward(self, steps: int) -> str:
        if steps > len(self.web) - self.curr - 1: # more steps than elements in front
            self.curr = len(self.web) - 1
            return self.web[self.curr]
        else:
            self.curr += steps
            return self.web[self.curr]
       
        
# Time complexity:
# visit - O(n) since slicing operation creates a new list everytime, worst case copies entire list
# back/forward: O(1) at worst since all elements already indexed

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)