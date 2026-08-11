import heapq
class SeatManager:
    # invariant that there are n seats, unreserved() will garuntee a reserved seat, atleast one seat will be empty when calling reserve()
    # DS: minHeap for log(n) insert and delete 
    def __init__(self, n: int):
        self.tables = [i for i in range(1,n+1)] # no need to heapify, already has heap property(children larger)

    def reserve(self) -> int:
        return heapq.heappop(self.tables)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.tables, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)