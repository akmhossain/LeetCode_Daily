# invariant that there are five types of banknotes, deposit smallest-->largest, withdraw-->largest to smallest
class ATM:
    def __init__(self):
        self.bank = [0,0,0,0,0] # 500 --> 20

    def deposit(self, banknotesCount: List[int]) -> None:
        ptr = 4
        for i in range(5):
            self.bank[ptr] += banknotesCount[i]
            ptr -= 1
        
    def withdraw(self, amount: int) -> List[int]:
    # start with highest denomintaion, check if there are lower ones that match
        ptr = 0
        values = [500, 200, 100, 50, 20]
        res = [0, 0, 0, 0, 0]
        
        for i in range(5):
            needed = amount // values[i]
            amount_allowed = min(needed, self.bank[i]) # take as much as needed, not more than availible
            amount -= values[i] * amount_allowed 
            res[i] = amount_allowed

        if amount == 0:
            for i in range(5):
              self.bank[i] -= res[i]
            res.reverse()
            return res
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)