import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # given [userID, taskID, priority]
        # heap: priority,taskID
        # hashmap: taskID --> priority (for fast lookup in heap)
        # lazy deletion: only hashmap has valid entries, queue can have stale entries

        self.get_priority = {}
        self.pq = []
        for task in tasks:
            userID, taskID, priority = task[0], task[1], task[2]
            self.pq.append((-priority, -taskID))
            self.get_priority[taskID] = (userID, priority)
        
        heapq.heapify(self.pq)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.get_priority[taskId] = (userId, priority)
        heapq.heappush(self.pq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userID = self.get_priority[taskId][0]
        self.get_priority[taskId] = (userID, newPriority)
        heapq.heappush(self.pq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.get_priority[taskId]

    def execTop(self) -> int:
        while self.pq:
            priority_neg, taskID_neg = heapq.heappop(self.pq)
            taskID = -taskID_neg

            if (taskID not in self.get_priority) or (-priority_neg != self.get_priority[taskID][1]):
                continue
            
            userID = self.get_priority[taskID][0]
            del self.get_priority[taskID]
            return userID
        
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()