from collections import defaultdict
class UndergroundSystem:
    # invariant that atleast one customer has travelled the route before getavgtime, time is chronological, customer is checked into one place at a time
    # double hash map solution 
    # checked_in: id --> [stationName, time] 
    # totals: route[start, end] --> totalTime, count
    def __init__(self):
        self.checked_in = defaultdict(list)
        self.totals = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checked_in: # already checked in
            return
        else:
            self.checked_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # retrieve station name and entry time
        # remove customer from checkIn
        # [startName, endName] += t - entry time 
        entry_station, entry_time = self.checked_in[id]
        del self.checked_in[id]
        trip_time = t - entry_time
        route = (entry_station, stationName)

        if route not in self.totals:
            self.totals[route] = [0, 0]  # [total_time, count]

        self.totals[route][0] += trip_time
        self.totals[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # check if there are any trips from start to end station
        total, count = self.totals[(startStation, endStation)]
        return total/count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)